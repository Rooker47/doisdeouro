# Generated by Django 3.1 on 2020-09-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAlmox', '0004_auto_20200906_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saida',
            name='material',
            field=models.CharField(max_length=100),
        ),
    ]
