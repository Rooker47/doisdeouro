# Generated by Django 3.1 on 2020-09-08 23:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appAlmox', '0012_auto_20200908_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='saida',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]