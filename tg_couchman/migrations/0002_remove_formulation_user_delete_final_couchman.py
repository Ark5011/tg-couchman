# Generated by Django 5.0.6 on 2024-08-05 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tg_couchman', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Final_Couchman',
        ),
    ]
