# Generated by Django 5.0.6 on 2024-07-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.FloatField()),
                ('casein', models.FloatField()),
                ('whey_protein', models.FloatField()),
                ('lactose', models.FloatField()),
                ('GOS', models.FloatField()),
                ('PDX', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Final_Tg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_tg_min', models.FloatField()),
                ('final_tg_target', models.FloatField()),
                ('final_tg_max', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Formulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_min', models.FloatField()),
                ('casein', models.FloatField()),
                ('whey_protein', models.FloatField()),
                ('GOS', models.FloatField()),
                ('PDX', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('more_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.FloatField()),
                ('casein', models.FloatField()),
                ('whey_protein', models.FloatField()),
                ('lactose', models.FloatField()),
                ('GOS', models.FloatField()),
                ('PDX', models.FloatField()),
            ],
        ),
    ]
