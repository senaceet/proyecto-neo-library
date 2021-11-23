from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404

from .forms import DocumetoForm,UserForm,Clientform,Editorialform,Writerform,tagform,Bookform
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
#books page
def books (request):
    tag = tagform()
    writer = Writerform()
    editorial = Editorialform()
    book = Bookform()
    #save tag
    if request.method == 'POST' and 'tagsavebtn' in request.POST:
        filled_form = tagform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Etiqueta %s guardada correctamente' %(filled_form.cleaned_data['name_tag'])
            new_form = DocumetoForm()
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note})
    #save editorial
    if request.method == 'POST' and 'editorialsavebtn' in request.POST:
        filled_form = Editorialform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'editorial %s guardada correctamente' %(filled_form.cleaned_data['name_editorial'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note})
    #save writer
    if request.method == 'POST' and 'writersavebtn' in request.POST:
        filled_form = Writerform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Autor(a) %s guardado correctamente' %(filled_form.cleaned_data['name_writer'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note})
    if request.method == 'POST' and 'savebookbtn1' in request.POST:
        filled_form =Bookform(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            note = 'libro %s guardado correctamente' %(filled_form.cleaned_data['title'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note})
    else:    
        return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book})
def my_loans (request,Cliient_id): #teasting
    try:
        client = Cliient.objects.get(id=Cliient_id)
    except Cliient.DoesNotExist:
        raise Http404('client not found')
    return render (request,'mis_prestamos.html',{'client':client,})
def loans (request):
    return  render (request,'prestamos.html')
#users page
def users (request):
    clients = Cliient.objects
    #show info for modify
    if request.method == 'GET' and 'showinfouserbtn1' in request.GET:
        p=(request.GET)
        pk = p['clientid']
        form1 = DocumetoForm()
        form2 =UserForm()
        M_client = Useer.objects.filter(cliient=pk).first()
        M_form =  UserForm(instance=M_client)
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'modify_client':M_client,'modify_form':M_form,'p':p,'pk_client':pk})
    # save modify user
    if request.method == 'POST' and 'usermodifyformbtn2' in request.POST:
        p=(request.POST)
        pk = p['clientid']
        M_client = Useer.objects.filter(cliient=pk).first()
        M_form =  UserForm(instance=M_client)
        filled_form = UserForm(request.POST,instance=M_client)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Usuario: %s %s - %s, modificado exitosamente' %(filled_form.cleaned_data['first_name'],filled_form.cleaned_data['surname'],filled_form.cleaned_data['document_user'],)
            form1 = DocumetoForm()
            form2 =UserForm()
            return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'note':note})
    #crear tipo de documento
    if request.method == 'POST' and 'Documenttypeformbtn1' in request.POST:
        filled_form = DocumetoForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Documento: %s - %s, guardado exitosamente' %(filled_form.cleaned_data['acronym_doc'],filled_form.cleaned_data['nomb_type_document'],)
            new_form = DocumetoForm()
            return render (request,'usuarios.html', {'clients':clients,'documentoform':new_form, 'note':note,'usuarioform':UserForm,})
    #crear usuario
    if request.method == 'POST' and 'userformbtn1' in request.POST:
       filled_form =UserForm(request.POST)
       if filled_form.is_valid():
            created_user = filled_form.save()
            created_userpk = created_user.id
            client = Clientform({'fk_id_user':created_userpk})
            client.save() 
            note = 'Usuario: %s %s - %s, guardado exitosamente' %(filled_form.cleaned_data['first_name'],filled_form.cleaned_data['surname'],filled_form.cleaned_data['document_user'],)
            new_form =UserForm()
            return render (request,'usuarios.html', {'created_userpk':created_userpk,'clients':clients,'usuarioform':new_form,'documentoform':DocumetoForm, 'note':note,})
    #show info for deleted user
    if request.method == 'GET' and 'deleteuserbtn1' in request.GET:
        d = (request.GET)
        pk = d['clientid']
        form1 = DocumetoForm()
        form2 =UserForm()
        D_client = Useer.objects.filter(cliient=pk).first()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'delte_client':D_client,'d':d,'pk_client':pk})
    #confir delete user
    if request.method == 'POST' and 'confirdeletebtn1' in request.POST:
        d=(request.POST)
        pk = d['clientid']
        Useer.objects.filter(cliient=pk).delete()
        form1 = DocumetoForm()
        form2 =UserForm()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,})
        
    #default
    else:
        form1 = DocumetoForm()
        form2 =UserForm()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,})
def booksinfo (request):
    return render (request,'infolibro.html')