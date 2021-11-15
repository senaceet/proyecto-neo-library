from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404

from .forms import DocumetoForm,UserForm,Clientform
from .models import Cliient,Useer

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
def my_loans (request,Cliient_id): #teasting
    try:
        client = Cliient.objects.get(id=Cliient_id)
    except Cliient.DoesNotExist:
        raise Http404('client not found')
    return render (request,'mis_prestamos.html',{'client':client,})
def loans (request):
    return  render (request,'prestamos.html')
def users (request):
    clients = Cliient.objects
    if request.method == 'POST' and 'Documenttypeformbtn1' in request.POST:
        filled_form = DocumetoForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Documento: %s - %s, guardado exitosamente' %(filled_form.cleaned_data['acronym_doc'],filled_form.cleaned_data['nomb_type_document'],)
            new_form = DocumetoForm()
            return render (request,'usuarios.html', {'clients':clients,'documentoform':new_form, 'note':note,'usuarioform':UserForm})
    if request.method == 'POST' and 'userformbtn1' in request.POST:
       filled_form =UserForm(request.POST)
       if filled_form.is_valid():
            created_user = filled_form.save()
            created_userpk = created_user.id
            client = Clientform({'fk_id_user':created_userpk})
            client.save() 
            note = 'Usuario: %s %s - %s, guardado exitosamente' %(filled_form.cleaned_data['first_name'],filled_form.cleaned_data['surname'],filled_form.cleaned_data['document_user'],)
            new_form =UserForm()
            return render (request,'usuarios.html', {'clients':clients,'usuarioform':new_form,'documentoform':DocumetoForm, 'note':note})
    else:
        form1 = DocumetoForm()
        form2 =UserForm()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2})
def booksinfo (request):
    return render (request,'infolibro.html')