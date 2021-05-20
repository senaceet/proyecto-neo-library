from django.contrib import admin

from .models import DocumentType,Useer,Book,Loan,Cliient,Admin,Writer,Genre,Editorial

admin.site.register(DocumentType)
admin.site.register(Useer)
admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(Cliient)
admin.site.register(Admin)
admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Editorial)