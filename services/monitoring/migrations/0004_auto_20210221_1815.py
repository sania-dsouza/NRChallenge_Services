# Generated by Django 3.1.7 on 2021-02-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0003_auto_20210221_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='co2_emission',
            name='measured_date',
            field=models.DateField(),
        ),
    ]