from django.shortcuts import render

def index (request):
    return render(request,'index.html')
def log_admin (request):
    return render(request,'loginad.html')
def log_user (request):
    return render(request,'loginus.html')
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