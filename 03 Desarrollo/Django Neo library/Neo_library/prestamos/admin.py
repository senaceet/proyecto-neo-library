from django.contrib import admin

from .models import DocumentType,Useer,Book,Loan,Cliient,Admin

admin.site.register(DocumentType)
admin.site.register(Useer)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Cliient)
admin.site.register(Admin)
