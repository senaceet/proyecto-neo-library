# Generated by Django 3.2.3 on 2021-06-20 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0010_auto_20210527_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useer',
            name='document_user',
            field=models.CharField(max_length=25, verbose_name='Numero de documento'),
        ),
    ]
