from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return render(request, 'auth/login.html',)

        else:
            error_message=form.errors.as_text()
            return render(request, 'auth/register.html',{'message':error_message})

    return render(request, 'auth/register.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')