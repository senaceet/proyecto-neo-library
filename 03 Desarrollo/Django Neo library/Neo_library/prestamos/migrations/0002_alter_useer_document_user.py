# Generated by Django 3.2.3 on 2021-05-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useer',
            name='document_user',
            field=models.IntegerField(),
        ),
    ]