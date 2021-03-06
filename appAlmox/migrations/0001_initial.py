# Generated by Django 3.1 on 2020-09-06 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appCreate', '0003_auto_20200905_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100, unique=True)),
                ('quant', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('nf', models.CharField(max_length=10, unique=True, verbose_name='nota Fiscal')),
            ],
            options={
                'ordering': ('material',),
            },
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=100, unique=True)),
                ('quant', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('destino', models.CharField(max_length=20)),
                ('recebedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCreate.pessoa')),
            ],
            options={
                'ordering': ('material',),
            },
        ),
    ]
