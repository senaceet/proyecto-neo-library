from django import forms
from .models import DocumentType

#class DocumetoForm(forms.Form):
#   siglas = forms.CharField(label='siglas',max_length=100)
#  document = forms.CharField(label='tipo de documento',max_length=100)

class  DocumetoForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = ['nomb_type_document','acronym_doc']
        labels = {'nomb_type_document':'Tipo de Documento','acronym_doc':'Siglas'}