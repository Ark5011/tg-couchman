# Generated by Django 5.0.6 on 2024-08-06 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tg_couchman', '0002_remove_formulation_user_delete_final_couchman'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cp',
        ),
        migrations.DeleteModel(
            name='Tg',
        ),
    ]
