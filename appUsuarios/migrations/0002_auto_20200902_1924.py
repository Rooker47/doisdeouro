# Generated by Django 3.1 on 2020-09-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nomeCompletoUsuario',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
