from django.db import models
from django.db.models.fields import CharField

class DocumentType(models.Model):
    nomb_type_document = models.CharField(max_length=25)
    acronym_doc = models.CharField(max_length=10)

    def __str__(self):
        return self.acronym_doc
    class Meta:
        db_table = 'document_type'

class Editorial(models.Model):
    name_editorial = models.CharField(max_length=45)

    def __str__(self):
        return self.name_editorial
    class Meta:
        db_table = 'Editorial'
class Writer(models.Model):
    name_writer = models.CharField(max_length=50)

    def __str__(self):
        return self.name_editorial

    class Meta:
        db_table = 'writer'

class Genre(models.Model):
    name_genre = models.CharField(max_length=30)

    def __str__(self):
        return self.name_genre
    class Meta:
        db_table = 'genre'

class Useer(models.Model):
    document_user = models.IntegerField()
    fk_type_document = models.ForeignKey(DocumentType,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    sec_name = models.CharField(blank=True, null=True,max_length=15)
    surname = models.CharField(max_length=15)
    sec_surname = models.CharField(blank=True, null=True,max_length=15)
    password_ad = models.CharField(max_length=12)
    email = models.EmailField(max_length=111)
    address = models.CharField(max_length=20)
    cell_phone = models.BigIntegerField()

    def __str__(self):
        return self.document_user+' '+self.first_name+' '+self.surname

    class Meta:
        db_table = 'useer'
class Admin(models.Model):
    fk_id_user = models.ForeignKey(Useer,on_delete=models.CASCADE)

    class Meta:
        db_table = 'admin'


class Book(models.Model):
    AVAILABILITY_CHOISES = [('D','disponible'),('N', 'no disponible')]
    barcode = models.CharField(blank=True, null=True,max_length=30)
    title = models.CharField(max_length=40)
    availability = models.CharField(max_length=14,choices=AVAILABILITY_CHOISES)
    coments = models.TextField(blank=True, null=True)
    fk_editorial = models.ForeignKey(Editorial,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'

class Cliient(models.Model):
    fk_id_user = models.ForeignKey(Useer,on_delete=models.CASCADE)
    observation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'cliient'

class Loan(models.Model):
    date_loan = models.DateTimeField(auto_now=True)
    return_date = models.DateField()
    current_state = models.TextField()  
    coment = models.TextField(blank=True, null=True)
    fk_id_client = models.ForeignKey(Cliient,on_delete=models.CASCADE)

    class Meta:
        db_table = 'loan'


class LogError(models.Model):
    description_error = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log_error'


class ServerMail(models.Model):
    mail = models.EmailField(blank=True, null=True)

    class Meta:
        db_table = 'server_mail'