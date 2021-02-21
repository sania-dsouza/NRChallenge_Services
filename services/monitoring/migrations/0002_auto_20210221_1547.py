# Generated by Django 3.1.7 on 2021-02-21 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='co2_emission',
            name='measured_at',
        ),
        migrations.RemoveField(
            model_name='nox_emission',
            name='measured_at',
        ),
        migrations.RemoveField(
            model_name='so2_emission',
            name='measured_at',
        ),
        migrations.AddField(
            model_name='co2_emission',
            name='measured_at_minute',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='co2_emission',
            name='measured_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nox_emission',
            name='measured_at_minute',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='nox_emission',
            name='measured_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='so2_emission',
            name='measured_at_minute',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='so2_emission',
            name='measured_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]