# Generated by Django 3.1.7 on 2021-02-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CO2_Emission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emission_Mt', models.PositiveSmallIntegerField()),
                ('measured_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NOX_Emission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emission_Mt', models.PositiveSmallIntegerField()),
                ('measured_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SO2_Emission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emission_Mt', models.PositiveSmallIntegerField()),
                ('measured_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
