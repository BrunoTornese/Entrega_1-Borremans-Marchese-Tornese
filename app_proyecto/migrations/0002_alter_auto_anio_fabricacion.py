# Generated by Django 4.0.5 on 2022-07-09 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='anio_fabricacion',
            field=models.DateField(),
        ),
    ]
