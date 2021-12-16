from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import logout
from django.contrib import messages
from django.http import Http404

from .forms import DocumetoForm,UserForm,Clientform,Editorialform,Writerform,tagform,Bookform,Loanform,UserRegisterForm
from .models import Cliient,Useer,Book,Loan
from .decorators import unauthenticated_user,allowed_users

def index (request):
    books=Book.objects.all()
    if request.user.is_authenticated:
        user = request.user
        client = Cliient.objects.filter(fk_id_user=user.id).first()
        if client != None:
            client_id = client.id
            return render(request,'index.html',{'books':books,'client':client_id})
    return render(request,'index.html',{'books':books,})
#log in as user
@unauthenticated_user
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
#funcion de logout
def logout_view (request):
    logout (request)
    messages.success(request,'sesion finalizada')
    return redirect('index')
#administracion page
@login_required(login_url='log_user') ##decorator automatico django
@allowed_users(allowed_roles=['librarian'])
def administration (request):
    n_loan = Loanform()
    book = Bookform()
    n_user = UserForm()
    nn_user= UserRegisterForm()
    #contadores
    #contador de usuario
    number_users = Cliient.objects.count()
    #contador libros
    number_books = Book.objects.count()
    #contador de prestamos
    number_loans = Loan.objects.count()
    #last loans
    last_loans=Loan.objects.all().order_by('-id')[:10]
    #save loan
    if request.method == 'POST' and 'saveloanbtn' in request.POST:
        filled_form =Loanform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'prestamo con fecha de devolucion %s guardado correctamente' %(filled_form.cleaned_data['return_date'])
            return render (request,'administracion.html',{'newloan':n_loan,'note':note,'libroform':book,'usuarioform':n_user,'n_u':number_users,'n_b':number_books,'n_l':number_loans,'last_l':last_loans,'usuario1form':nn_user})
    #save user
    if request.method == 'POST' and 'saveuserbtn' in request.POST:
       filled_form =UserRegisterForm(request.POST)
       filled_form2 = UserForm(request.POST)
       if filled_form.is_valid():
            created_user = filled_form.save()
            created_userpk = created_user.id
            client = Clientform({'fk_id_user':created_userpk})
            client.save()
            profile=filled_form2.save(commit=False)
            profile.user = created_user
            profile.save()
            note = 'Usuario: %s %s -guardado exitosamente' %(filled_form.cleaned_data['first_name'],filled_form.cleaned_data['last_name'],)
            return render (request,'administracion.html',{'newloan':n_loan,'note':note,'libroform':book,'usuario1form':nn_user,'usuarioform':n_user,'n_u':number_users,'n_b':number_books,'n_l':number_loans,'last_l':last_loans,})
    #save book
    if request.method == 'POST' and 'savebookbtn' in request.POST:
        filled_form =Bookform(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            note = 'libro %s guardado correctamente' %(filled_form.cleaned_data['title'])
            return render (request,'administracion.html',{'newloan':n_loan,'note':note,'libroform':book,'usuarioform':n_user,'n_u':number_users,'n_b':number_books,'n_l':number_loans,'last_l':last_loans,'usuario1form':nn_user})
    return render (request,'administracion.html',{'newloan':n_loan,'libroform':book,'usuarioform':n_user,'n_u':number_users,'n_b':number_books,'n_l':number_loans,'last_l':last_loans,'usuario1form':nn_user})
#books page
@login_required(login_url='log_user') ##decorator automatico django
@allowed_users(allowed_roles=['librarian'])
def books (request):
    libros = Book.objects.all()
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
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note,'books':libros})
    #save editorial
    if request.method == 'POST' and 'editorialsavebtn' in request.POST:
        filled_form = Editorialform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'editorial %s guardada correctamente' %(filled_form.cleaned_data['name_editorial'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note,'books':libros})
    #save writer
    if request.method == 'POST' and 'writersavebtn' in request.POST:
        filled_form = Writerform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Autor(a) %s guardado correctamente' %(filled_form.cleaned_data['name_writer'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note,'books':libros})
    #save book
    if request.method == 'POST' and 'savebookbtn1' in request.POST:
        filled_form =Bookform(request.POST, request.FILES)
        if filled_form.is_valid():
            filled_form.save()
            note = 'libro %s guardado correctamente' %(filled_form.cleaned_data['title'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note,'books':libros})
    #show book info
    if request.method == 'GET' and 'infobookbtn' in request.GET:
        i = (request.GET)
        pk = i['bookid']
        infobook = Book.objects.filter(pk=pk).first()
        infobform = Bookform(instance=infobook)
        return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'books':libros,'i':i,'infofrom':infobform,'infobook':infobook})
    # save modify book info
    if request.method == 'POST' and 'editbookbtn' in request.POST:
        i = (request.POST)
        pk = i['bookid']
        m_book = Book.objects.filter(pk=pk).first()
        mb_form =  Bookform(instance=m_book)
        filled_form = Bookform(request.POST,request.FILES,instance=m_book)
        if filled_form.is_valid():
            filled_form.save()
            note = 'libro %s modificado correctamente' %(filled_form.cleaned_data['title'])
            return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'note':note,'books':libros})
    # delete warning book
    if request.method == 'POST' and 'deletebookbtn' in request.POST:
        db = (request.POST)
        pk = db['bookid']
        d_book = Book.objects.filter(pk=pk).first()
        return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'books':libros,'db':db,'d_book':d_book})
    #confirm delete book
    if request.method == 'POST' and 'confirdeletebtn' in request.POST:
        db = (request.POST)
        pk = db['bookid']
        Book.objects.filter(pk=pk).delete()
        return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'books':libros})
    else:    
        return render (request,'libros.html',{'etiquetaform':tag,'escritorform':writer,'editorialform':editorial,'libroform':book,'books':libros})
#pagina mis prestamos
@login_required(login_url='log_user') ##decorator automatico django
def my_loans (request,Cliient_id): #teasting
    try:
        client = Cliient.objects.get(id=Cliient_id)
        c_loans = Loan.objects.filter(fk_id_client=client.pk)[:7]
        #show info loan
        if request.method == 'GET' and 'smloanbtn' in request.GET:
            i = (request.GET)
            pk = i['loanid']
            infoloan= Loan.objects.filter(pk=pk).first()
            infoloanform = Loanform(instance=infoloan)
            return render (request,'mis_prestamos.html',{'client':client,'c_loans':c_loans,'infoloan':infoloan,'ifoform':infoloanform,'i':i})
    except Cliient.DoesNotExist:
        raise Http404('client not found')
    return render (request,'mis_prestamos.html',{'client':client,'c_loans':c_loans,})
# loans page
@login_required(login_url='log_user') ##decorator automatico django
@allowed_users(allowed_roles=['librarian'])
def loans (request):
    prestamos=Loan.objects.all
    n_loan = Loanform()
    #save loan
    if request.method == 'POST' and 'loansavebtn' in request.POST:
        filled_form =Loanform(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = 'prestamo con fecha de devolucion %s guardado correctamente' %(filled_form.cleaned_data['return_date'])
        return  render (request,'prestamos.html',{'newloan':n_loan,'note':note,'loans':prestamos})
    #show info loan
    if request.method == 'GET' and 'smloanbtn' in request.GET:
        i = (request.GET)
        pk = i['loanid']
        infoloan= Loan.objects.filter(pk=pk).first()
        infoloanform = Loanform(instance=infoloan) 
        return  render (request,'prestamos.html',{'newloan':n_loan,'loans':prestamos,'infoloan':infoloan,'ifoform':infoloanform,'i':i})
    # save modify book loan
    if request.method == 'POST' and 'savemodloanbtn' in request.POST:
        i = (request.POST)
        pk = i['loanid']
        m_loan = Loan.objects.filter(pk=pk).first()
        ml_form =  Loanform(instance=m_loan)
        filled_form = Loanform(request.POST,instance=m_loan)
        if filled_form.is_valid():
            filled_form.save()
            note = 'prestamo modificado correctamente'
            return  render (request,'prestamos.html',{'newloan':n_loan,'loans':prestamos,'note':note})
    # delete warning loan
    if request.method == 'POST' and 'deleteloanbtn' in request.POST:
        dl = (request.POST)
        pk = dl['loanid']
        d_loan = Loan.objects.filter(pk=pk).first()
        return  render (request,'prestamos.html',{'newloan':n_loan,'loans':prestamos,'dl':dl,'d_loan':d_loan})
    # delete confirm loan
    if request.method == 'POST' and 'confirdeletebtn' in request.POST:
        dl = (request.POST)
        pk = dl['bookid']
        Loan.objects.filter(pk=pk).delete()
        return  render (request,'prestamos.html',{'newloan':n_loan,'loans':prestamos})
    return  render (request,'prestamos.html',{'newloan':n_loan,'loans':prestamos})
#users page
@login_required(login_url='log_user') ##decorator automatico django
@allowed_users(allowed_roles=['librarian'])
def users (request):
    clients = Cliient.objects
    #show info for modify
    if request.method == 'GET' and 'showinfouserbtn1' in request.GET:
        p=(request.GET)
        pk = p['clientid']
        form1 = DocumetoForm()
        form2 =UserForm()
        form3 = UserRegisterForm()
        form4 = UserChangeForm()
        M_client = User.objects.filter(cliient=pk).first()
        M_client2 = Useer.objects.filter(user=M_client.pk).first()
        M_form =  UserChangeForm(instance=M_client)
        M_form2 = UserForm(instance=M_client2)
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'userform':form3,'modifyf':form4,'modify_client':M_client,'modify_form':M_form,'p':p,'pk_client':pk,'modify_form1':M_form2,})
    # save modify user
    if request.method == 'POST' and 'usermodifyformbtn2' in request.POST:
        p=(request.POST)
        pk = p['clientid']
        M_client = User.objects.filter(cliient=pk).first()
        M_client2 = Useer.objects.filter(user=M_client.pk).first()
        M_form = UserChangeForm(instance=M_client)
        M_form2 =  UserForm(instance=M_client2)
        filled_form = UserChangeForm(request.POST,instance=M_client,)
        filled_form2 = UserForm(request.POST,instance=M_client2)
        if filled_form.is_valid():
            filled_form.save()
            filled_form2.save()
            note = 'Usuario: %s %s -, modificado exitosamente' %(filled_form.cleaned_data['first_name'],filled_form.cleaned_data['last_name'],)
            form1 = DocumetoForm()
            form2 = UserForm()
            form3 = UserRegisterForm()
            form4 = UserChangeForm()
            return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'note':note,'userform':form3,'modifyf':form4})
        else:
           print (filled_form.errors) #To see the form errors in the console
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
       filled_form =UserRegisterForm(request.POST)
       filled_form2 = UserForm(request.POST)
       if filled_form.is_valid():
            created_user = filled_form.save()
            created_userpk = created_user.id
            client = Clientform({'fk_id_user':created_userpk})
            client.save()
            profile=filled_form2.save(commit=False)
            profile.user = created_user
            profile.save()
            note = 'Usuario: %s %s -, guardado exitosamente' %(filled_form.cleaned_data['first_name'],filled_form.cleaned_data['last_name'],)
            new_form =UserForm()
            return render (request,'usuarios.html', {'created_userpk':created_userpk,'clients':clients,'usuarioform':new_form,'documentoform':DocumetoForm, 'note':note,})
    #show info for deleted user
    if request.method == 'GET' and 'deleteuserbtn1' in request.GET:
        d = (request.GET)
        pk = d['clientid']
        form1 = DocumetoForm()
        form2 =UserForm()
        form3 = UserRegisterForm()
        form4 = UserChangeForm()
        D_client = User.objects.filter(cliient=pk).first()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'delte_client':D_client,'d':d,'pk_client':pk,'userform':form3,'modifyf':form4})
    #confir delete user
    if request.method == 'POST' and 'confirdeletebtn1' in request.POST:
        d=(request.POST)
        pk = d['clientid']
        User.objects.filter(cliient=pk).delete()
        form1 = DocumetoForm()
        form2 =UserForm()
        form3 = UserRegisterForm()
        form4 = UserChangeForm()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'userform':form3,'modifyf':form4})
        
    #default
    else:
        form1 = DocumetoForm()
        form2 =UserForm()
        form3 = UserRegisterForm()
        form4 = UserChangeForm()
        return render (request,'usuarios.html', {'clients':clients,'documentoform':form1,'usuarioform':form2,'userform':form3,'modifyf':form4})
#info book page
def booksinfo (request,Book_id):
    try:
        book = Book.objects.get(id=Book_id)
        releted_books_autor = Book.objects.filter(fk_writer__in=book.fk_writer.all()).exclude(pk=book.pk)[:3]
        releted_books_tag = Book.objects.filter(fk_tag__in=book.fk_tag.all()).exclude(pk=book.pk)[:3]
    except Cliient.DoesNotExist:
        raise Http404('libro no encontrado')
    return render (request,'infolibro.html',{'book':book,'ra_books':releted_books_autor,'rt_books':releted_books_tag,})
#test register
@unauthenticated_user
def register (request):
    form = UserRegisterForm()
    form1 = UserForm()
    if request.method == 'POST':
        filled_form = UserRegisterForm(request.POST)
        filled_form2 = UserForm(request.POST)
        if filled_form.is_valid():
            user = filled_form.save()
            profile=filled_form2.save(commit=False)
            profile.user = user
            profile.save()
            username = filled_form.cleaned_data.get('username')
            messages.success(request, f'hi{user}, youre register')
            return redirect('index')
    return render(request,'register.html',{'form':form,'form1':form1})