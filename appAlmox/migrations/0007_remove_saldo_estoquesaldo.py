# Generated by Django 3.1 on 2020-09-08 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appAlmox', '0006_auto_20200908_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saldo',
            name='estoqueSaldo',
        ),
    ]