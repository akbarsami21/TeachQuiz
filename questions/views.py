from django.shortcuts import render
from .models import Course, Question, ScoreBoard
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max
from django.db.models import F, Subquery, OuterRef

import json

@login_required(login_url='/login')
def index(request):
    course = Course.objects.all()
    return render(request, 'index.html', {'course': course})

@login_required(login_url='/login')
def take_quiz(request, id):
    context = {'id': id}
    return render(request, 'quiz.html', context)

@login_required(login_url='/login')
def api_quesiton(request, id):
    if not request.user.is_superuser:
        return redirect('/')
    raw_question = Question.objects.filter(course=id)[:20]
    questionset = []
    for q in raw_question:
        question = {
            'id': q.id,  # Ensure the ID is included
            'question': q.question,
            'answer': q.answer,
            'marks': q.marks,
            'options': [q.options_one, q.options_two]
        }
        if q.options_three:
            question['options'].append(q.options_three)
        if q.options_four:
            question['options'].append(q.options_four)
        questionset.append(question)

    return JsonResponse(questionset, safe=False)

@login_required(login_url='/login')
def view_score(request):
    user = request.user
    latest_scores_subquery = ScoreBoard.objects.filter(
        user=user,
        course=OuterRef('course')
    ).order_by('-id')

    scores = ScoreBoard.objects.filter(user=user).values(
        'course__name'
    ).annotate(
        highest_score=Max('score'),
        latest_score=Subquery(latest_scores_subquery.values('score')[:1])
    ).order_by('course__name')

    return render(request, 'score.html', {'scores': scores})

@csrf_exempt
@login_required(login_url='/login')
def check_score(request):
    data = json.loads(request.body)
    user = request.user
    course_id = data.get('course_id')
    solutions = json.loads(data.get('data'))
    course = Course.objects.get(id=course_id)
    score = 0

    for solution in solutions:
        question = Question.objects.filter(id=solution['question_id']).first()
        if question.answer == solution['option']:
            score += question.marks

    scoreboard = ScoreBoard(user=user, course=course, score=score)
    scoreboard.save()
    return JsonResponse({'message': 'success', 'status': True})
