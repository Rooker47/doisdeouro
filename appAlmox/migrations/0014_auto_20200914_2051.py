# Generated by Django 3.1 on 2020-09-14 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPrimeiraSecao', '0001_initial'),
        ('appAlmox', '0013_auto_20200908_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saida',
            name='recebedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrimeiraSecao.pessoa'),
        ),
    ]
