# Generated by Django 3.2.3 on 2021-11-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0015_alter_loan_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='name_genre',
            new_name='name_tag',
        ),
        migrations.AlterField(
            model_name='useer',
            name='cell_phone',
            field=models.CharField(max_length=25, verbose_name='Teléfono'),
        ),
    ]
