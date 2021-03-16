# Generated by Django 3.1.4 on 2021-03-16 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('service_interval', models.CharField(max_length=50)),
                ('next_service', models.CharField(max_length=50)),
                ('year', models.PositiveSmallIntegerField(default=2021, validators=[django.core.validators.MaxValueValidator(2021)])),
                ('length', models.CharField(max_length=100)),
                ('width', models.CharField(max_length=100)),
                ('HIN', models.CharField(blank=True, max_length=14, validators=[django.core.validators.MinLengthValidator(12)])),
                ('current_hours', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('service_interval', models.CharField(max_length=50)),
                ('next_service', models.CharField(max_length=50)),
                ('seats', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('VIN', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(11)])),
                ('current_mileage', models.PositiveSmallIntegerField()),
                ('year', models.IntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1886), django.core.validators.MaxValueValidator(2021)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('service_interval', models.CharField(max_length=50)),
                ('next_service', models.CharField(max_length=50)),
                ('seats', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=100)),
                ('VIN', models.CharField(max_length=17, validators=[django.core.validators.MinLengthValidator(11)])),
                ('current_mileage', models.PositiveSmallIntegerField()),
                ('year', models.IntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1896), django.core.validators.MaxValueValidator(2021)])),
                ('bed_length', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
