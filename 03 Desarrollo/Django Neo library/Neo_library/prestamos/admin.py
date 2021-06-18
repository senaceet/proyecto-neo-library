from django.contrib import admin
from django.db.models.base import Model
from .models import DocumentType,Useer,Book,Loan,Writer,Genre,Editorial
from import_export import resources
from import_export.admin import ImportExportModelAdmin

#admin.site.register(DocumentType)
@admin.register(DocumentType)
class DocumentType_admin(admin.ModelAdmin):
    list_display = ('nomb_type_document','acronym_doc')
    list_per_page = (5)
#admin.site.register(Useer)
@admin.register(Useer)
class  useer_admin(admin.ModelAdmin):
    list_display = ('first_name','surname','email')
    list_display_links = ('first_name','surname','email')
    search_fields = ('first_name','surname','email')
    list_filter = ('fk_type_document',)
    list_per_page = (10)
#admin.site.register(Book)
class bookresource(resources.ModelResource):

    class Meta:
        Model = Book
@admin.register(Book)
class Book_admin(admin.ModelAdmin):
    list_display = ('title','fk_editorial','availability')
    list_display_links = ('title','fk_editorial',)
    search_fields = ('title',)
    list_filter = ('fk_genre','availability','fk_editorial',)
    list_per_page = (10)
    resource_class = bookresource
#admin.site.register(Loan)
@admin.register(Loan)
class Loan_admin(admin.ModelAdmin):
    list_display = ('id','date_loan','return_date','current_state')
    list_display_links = ('id',)
    search_fields = ('fk_book','id','date_loan')
    list_filter = ('current_state',)
    list_per_page = (10)
#admin.site.register(Writer)
@admin.register(Writer)
class Writer_admin(admin.ModelAdmin):
    search_fields = ('name_writer',)
    list_per_page = (5)
#admin.site.register(Genre)
@admin.register(Genre)
class Genre_admin(admin.ModelAdmin):
    search_fields = ('name_genre',)
    list_per_page = (5)
#admin.site.register(Editorial)
@admin.register(Editorial)
class Editorial_admin(admin.ModelAdmin):
    search_fields = ('name_editorial',)
    list_per_page = (5)