# Generated by Django 3.1 on 2020-09-08 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCreate', '0003_auto_20200905_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guarnicao',
            name='vtr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appCreate.viatura', verbose_name='patrimônio'),
        ),
        migrations.AlterField(
            model_name='registrormb',
            name='arma',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appCreate.arma'),
        ),
    ]
