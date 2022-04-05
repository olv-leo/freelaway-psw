from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('confirm-password')

        if not password == password_confirmation:
            return redirect('/auth/cadastro')

        if not username.strip() or not password.strip():
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/auth/login')
        except:
            return redirect('/auth/cadastro')


def login(request):
    return HttpResponse('Login')
