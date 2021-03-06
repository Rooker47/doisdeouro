# Generated by Django 3.1 on 2020-09-06 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCreate', '0002_viatura_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guarnicao',
            name='vtr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCreate.viatura', unique=True, verbose_name='patrimônio'),
        ),
        migrations.AlterField(
            model_name='registrormb',
            name='arma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCreate.arma', unique=True),
        ),
        migrations.AlterField(
            model_name='viatura',
            name='status',
            field=models.BooleanField(default=None, verbose_name='Ativada'),
        ),
    ]
