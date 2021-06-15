from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages

def index (request):
    return render(request,'index.html')
def log_admin (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido')
            return redirect('administration')
        else:
            messages.error(request,'usuario o contraseña incorrecta')

    return render(request,'loginad.html')
def log_user (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            messages.success(request,'Bienvenido')
            return redirect('index')
        else:
            messages.error(request,'usuario o contraseña incorrecta')

    return render(request,'loginus.html')

def logout_view (request):
    logout (request)
    messages.success(request,'sesion finalizada')
    return redirect('log_admin')

def administration (request):
    return render (request,'administracion.html')
def books (request):
    return render (request,'libros.html')
def my_loans (request):
    return render (request,'mis_prestamos.html')
def loans (request):
    return  render (request,'prestamos.html')
def users (request):
    return render (request,'usuarios.html')