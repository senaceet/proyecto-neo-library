from django.contrib.admin.options import VERTICAL
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

class DocumentType(models.Model):
    nomb_type_document = models.CharField(max_length=25,verbose_name='Tipo de documento')
    acronym_doc = models.CharField(max_length=10,verbose_name='Siglas')

    def __str__(self):
        return self.acronym_doc
    class Meta:
        db_table = 'Tipo de documento'
        verbose_name= 'Tipo de Documento'
        verbose_name_plural= 'Tipos de Documentos'

class Editorial(models.Model):
    name_editorial = models.CharField(max_length=45,verbose_name='Editorial')

    def __str__(self):
        return self.name_editorial
    class Meta:
        db_table = 'Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural='Editoriales'
class Writer(models.Model):
    name_writer = models.CharField(max_length=50,verbose_name='Autor')

    def __str__(self):
        return self.name_writer

    class Meta:
        db_table = 'Autores'
        verbose_name = 'Autor'
        verbose_name_plural='Autores'


class tag(models.Model):
    name_tag = models.CharField(max_length=30,verbose_name='Etiquta')

    def __str__(self):
        return self.name_tag
    class Meta:
        db_table = 'Etiqutas'
        verbose_name = 'Etiquta'

class Useer(models.Model):
    document_user = models.CharField(max_length=25,verbose_name='Numero de documento')
    fk_type_document = models.ForeignKey(DocumentType,on_delete=models.CASCADE,verbose_name="Tipo de Documento")
    first_name = models.CharField(max_length=15,verbose_name='Primer Nombre')
    sec_name = models.CharField(blank=True, null=True,max_length=15,verbose_name='Segundo Nombre')
    surname = models.CharField(max_length=15,verbose_name='Primer Apellido')
    sec_surname = models.CharField(blank=True, null=True,max_length=15,verbose_name='Segundo Apellido')
    password_ad = models.CharField(max_length=20,verbose_name='Contraseña')
    email = models.EmailField(max_length=111,verbose_name='Correo')
    address = models.CharField(max_length=20,verbose_name='Dirección')
    cell_phone = models.CharField(max_length=25,verbose_name='Teléfono')

    class Meta:
        db_table = 'Usuarios'
        verbose_name = 'Usuario'

    def __str__(self):
        return self.document_user+' '+self.first_name+' '+self.surname

    
class Admin(models.Model):
    fk_id_user = models.ForeignKey(Useer,on_delete=models.CASCADE,verbose_name="Usuario")

    def __str__(self):
        return (self.fk_id_user)

    class Meta:
        db_table = 'Administradores'
        verbose_name = 'Administrador'
        verbose_name_plural='Administradores'


class Book(models.Model):
    barcode = models.CharField(blank=True, null=True,max_length=30,verbose_name='Codigo de barras')
    title = models.CharField(max_length=40,verbose_name='Titulo')
    availability = models.BooleanField(verbose_name='Disponibilidad',null=True)
    image = models.ImageField(verbose_name='Imagen',blank=True, null=True)
    Info = models.TextField(blank=True, null=True,verbose_name='Informacion')
    fk_editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE,verbose_name='Editorial')
    fk_writer = models.ManyToManyField(Writer,verbose_name='Escritor(es)')
    fk_tag =models.ManyToManyField(tag,verbose_name='Etiqueta(s)')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Libro'
        verbose_name = 'Libro'

class Cliient(models.Model):
    fk_id_user = models.ForeignKey(Useer,on_delete=models.CASCADE,verbose_name="Usuario")
    observation = models.TextField(blank=True, null=True,verbose_name='Comentario')

    def __str__(self):
        return str(self.fk_id_user)
    class Meta:
        db_table = 'clientes'
        verbose_name = 'cliente'

class Loan(models.Model):
    STATE_CHOISES = (('A','Activo'),('F', 'Finalizado'),('R','Retrazo'))
    date_loan = models.DateTimeField(auto_now=True,verbose_name='Fecha de préstamo')
    return_date = models.DateField(verbose_name='Fecha de devolucion')
    state = models.CharField(max_length=12,verbose_name='Estado',choices=STATE_CHOISES,null=True)
    coment = models.TextField(blank=True, null=True,verbose_name='Comentario')
    fk_id_client = models.ForeignKey(Cliient,on_delete=models.CASCADE,verbose_name='Usuario')
    fk_book = models.ManyToManyField(Book,verbose_name='Libro')

    class Meta:
        db_table = 'Prestamos'
        verbose_name = 'Préstamo'


class LogError(models.Model):
    description_error = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log_error'


class ServerMail(models.Model):
    mail = models.EmailField(blank=True, null=True)

    class Meta:
        db_table = 'server_mail'