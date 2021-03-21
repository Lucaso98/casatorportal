from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_page(request):
    if request.user.is_authenticated:
        return request('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(
                    request, 'Användarnamn ELLER Lösenord är inkorrekt')

    context = {}
    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def portal_page(request):
    return render(request, 'portalen/portalpage.html')
