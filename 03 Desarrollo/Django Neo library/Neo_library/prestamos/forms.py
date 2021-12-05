from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import DocumentType,Useer,Cliient,Editorial,Writer,tag,Book,Loan

class  DocumetoForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['nomb_type_document','acronym_doc']
        labels = {'nomb_type_document':'Tipo de Documento','acronym_doc':'Siglas'}

class UserForm(forms.ModelForm):
    class Meta:
        model = Useer
        fields = ['document_user','fk_type_document','address','cell_phone']

class Clientform(forms.ModelForm):
    class Meta:
        model = Cliient
        fields = ['fk_id_user']

class Editorialform(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'

class Writerform(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'

class tagform(forms.ModelForm):
    class Meta:
        model = tag
        fields = '__all__'

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['barcode']

class Loanform(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','last_name','first_name','email','password1','password2']