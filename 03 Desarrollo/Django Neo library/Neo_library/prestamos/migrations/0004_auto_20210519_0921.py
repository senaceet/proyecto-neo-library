# Generated by Django 3.2.3 on 2021-05-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0003_alter_cliient_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='fk_genre',
            field=models.ManyToManyField(to='prestamos.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='fk_writer',
            field=models.ManyToManyField(to='prestamos.Writer'),
        ),
        migrations.AlterField(
            model_name='book',
            name='availability',
            field=models.CharField(choices=[('D', 'disponible'), ('N', 'No disponible')], max_length=14, verbose_name='Disponivilidad'),
        ),
        migrations.AlterField(
            model_name='book',
            name='barcode',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Codigo de barras'),
        ),
        migrations.AlterField(
            model_name='book',
            name='coments',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='cliient',
            name='observation',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='acronym_doc',
            field=models.CharField(max_length=10, verbose_name='Siglas'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='nomb_type_document',
            field=models.CharField(max_length=25, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='name_editorial',
            field=models.CharField(max_length=45, verbose_name='Editorial'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name_genre',
            field=models.CharField(max_length=30, verbose_name='Genero'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='coment',
            field=models.TextField(blank=True, null=True, verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='current_state',
            field=models.CharField(max_length=15, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='date_loan',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de prestamo'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='return_date',
            field=models.DateField(verbose_name='Fecha de devolucion'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='address',
            field=models.CharField(max_length=20, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='cell_phone',
            field=models.BigIntegerField(verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='document_user',
            field=models.IntegerField(verbose_name='Numero de documento'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='email',
            field=models.EmailField(max_length=111, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='first_name',
            field=models.CharField(max_length=15, verbose_name='Primer Nombre'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='password_ad',
            field=models.CharField(max_length=12, verbose_name='Contraseña'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='sec_name',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Segundo Nombre'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='sec_surname',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Segundo Apellido'),
        ),
        migrations.AlterField(
            model_name='useer',
            name='surname',
            field=models.CharField(max_length=15, verbose_name='Primer Apellido'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='name_writer',
            field=models.CharField(max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterModelTable(
            name='admin',
            table='Administradores',
        ),
        migrations.AlterModelTable(
            name='book',
            table='Libro',
        ),
        migrations.AlterModelTable(
            name='cliient',
            table='clientes',
        ),
        migrations.AlterModelTable(
            name='documenttype',
            table='Tipo de documento',
        ),
        migrations.AlterModelTable(
            name='genre',
            table='Generos',
        ),
        migrations.AlterModelTable(
            name='loan',
            table='Prestamos',
        ),
        migrations.AlterModelTable(
            name='useer',
            table='Usuarios',
        ),
        migrations.AlterModelTable(
            name='writer',
            table='Autores',
        ),
    ]
