from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Användarnamnet ELLER lösenordet är inkorrekt.')

context = {}
return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def portal_page(request):
    return render(request, 'portalen/portalpage.html')
