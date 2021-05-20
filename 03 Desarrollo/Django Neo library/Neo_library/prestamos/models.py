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

class Editorial(models.Model):
    name_editorial = models.CharField(max_length=45,verbose_name='Editorial')

    def __str__(self):
        return self.name_editorial
    class Meta:
        db_table = 'Editorial'
class Writer(models.Model):
    name_writer = models.CharField(max_length=50,verbose_name='Autor')

    def __str__(self):
        return self.name_writer

    class Meta:
        db_table = 'Autores'

class Genre(models.Model):
    name_genre = models.CharField(max_length=30,verbose_name='Genero')

    def __str__(self):
        return self.name_genre
    class Meta:
        db_table = 'Generos'

class Useer(models.Model):
    document_user = models.IntegerField(verbose_name='Numero de documento')
    fk_type_document = models.ForeignKey(DocumentType,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15,verbose_name='Primer Nombre')
    sec_name = models.CharField(blank=True, null=True,max_length=15,verbose_name='Segundo Nombre')
    surname = models.CharField(max_length=15,verbose_name='Primer Apellido')
    sec_surname = models.CharField(blank=True, null=True,max_length=15,verbose_name='Segundo Apellido')
    password_ad = models.CharField(max_length=12,verbose_name='Contraseña')
    email = models.EmailField(max_length=111,verbose_name='Correo')
    address = models.CharField(max_length=20,verbose_name='Direccion')
    cell_phone = models.BigIntegerField(verbose_name='Telefono')

    class Meta:
        db_table = 'Usuarios'

    def __str__(self):
        return self.document_user+' '+self.first_name+' '+self.surname

    
class Admin(models.Model):
    fk_id_user = models.ForeignKey(Useer,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Administradores'


class Book(models.Model):
    AVAILABILITY_CHOISES = [('D','disponible'),('N', 'No disponible')]
    barcode = models.CharField(blank=True, null=True,max_length=30,verbose_name='Codigo de barras')
    title = models.CharField(max_length=40,verbose_name='Titulo')
    availability = models.CharField(max_length=14,choices=AVAILABILITY_CHOISES,verbose_name='Disponivilidad')
    image = models.ImageField(verbose_name='imagen',blank=True, null=True)
    coments = models.TextField(blank=True, null=True,verbose_name='Comentario')
    fk_editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)
    fk_writer = models.ManyToManyField(Writer)
    fk_genre =models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Libro'

class Cliient(models.Model):
    fk_id_user = models.ForeignKey(Useer,on_delete=models.CASCADE)
    observation = models.TextField(blank=True, null=True,verbose_name='Comentario')

    class Meta:
        db_table = 'clientes'

class Loan(models.Model):
    date_loan = models.DateTimeField(auto_now=True,verbose_name='Fecha de prestamo')
    return_date = models.DateField(verbose_name='Fecha de devolucion')
    current_state = models.CharField(verbose_name='Estado',max_length=15)
    coment = models.TextField(blank=True, null=True,verbose_name='Comentario')
    fk_id_client = models.ForeignKey(Cliient,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Prestamos'


class LogError(models.Model):
    description_error = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log_error'


class ServerMail(models.Model):
    mail = models.EmailField(blank=True, null=True)

    class Meta:
        db_table = 'server_mail'