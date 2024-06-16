from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.take_quiz, name='take_quiz'),  # Added trailing slash for consistency
    path('api/<int:id>/', views.api_quesiton, name='api_question'),  # Corrected variable type to int
    path('view_score/', views.view_score, name='view_score'),  # Added trailing slash for consistency
    path('api/check_score/', views.check_score, name='check_score'),  # Added missing path for check_score
]
