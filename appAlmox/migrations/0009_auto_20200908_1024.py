# Generated by Django 3.1 on 2020-09-08 13:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appAlmox', '0008_auto_20200908_1007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='nomeEntrada',
            new_name='nomeMaterialEntrada',
        ),
        migrations.RenameField(
            model_name='saida',
            old_name='materialSaidaEstoque',
            new_name='nomeMaterialSaida',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='movimento',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='quantEntrada',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='modificado',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='quantSaidaEstoque',
        ),
        migrations.AddField(
            model_name='entrada',
            name='quantMaterialEntrada',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='saida',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='saida',
            name='quantMaterialSaida',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='estoque_minimo',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='saida',
            name='destino',
            field=models.CharField(choices=[('P1', 'Primeira Seção'), ('P3', 'Terceira Seção'), ('P4', 'Quarta Seção'), ('Tes', 'Tesouraria'), ('Almox', 'Almoxarifado'), ('Almox', 'Almoxarifado'), ('Sec', 'Secretaria'), ('RMB', 'Material Bélico'), ('Transp', 'Seção de Transporte'), ('Com e TI', 'Seção de Comunicação e TI'), ('SsCOR', 'Correicional')], max_length=20),
        ),
    ]
