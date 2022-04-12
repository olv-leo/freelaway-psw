from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

def cadastro(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('confirm-password')

        if not password == password_confirmation:
            messages.add_message(request, constants.ERROR, 'As senhas digitadas precisam ser iguais.')
            return redirect('/auth/cadastro')

        if not username.strip() or not password.strip():
            messages.add_message(request, constants.ERROR, 'Todos os campos devem ser preenchidos.')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado.')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário salvo com sucesso!')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Falha ao salver o usuário.')
            return redirect('/auth/cadastro')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')

        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/')
    return HttpResponse('Login')

def sair(request):
    auth.logout(request)
    return redirect('/auth/login')
