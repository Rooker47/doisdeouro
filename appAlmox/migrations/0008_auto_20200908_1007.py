# Generated by Django 3.1 on 2020-09-08 13:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('appAlmox', '0007_remove_saldo_estoquesaldo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={},
        ),
        migrations.AlterModelOptions(
            name='saida',
            options={},
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='material',
            new_name='nomeEntrada',
        ),
        migrations.RenameField(
            model_name='entrada',
            old_name='quant',
            new_name='quantEntrada',
        ),
        migrations.RenameField(
            model_name='saida',
            old_name='material',
            new_name='materialSaidaEstoque',
        ),
        migrations.RenameField(
            model_name='saida',
            old_name='quant',
            new_name='quantSaidaEstoque',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='data',
        ),
        migrations.AddField(
            model_name='entrada',
            name='movimento',
            field=models.CharField(choices=[('e', 'entrada'), ('s', 'saida')], default='Escolha o tipo de movimento', max_length=1),
        ),
        migrations.AddField(
            model_name='saida',
            name='criado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='criado em:'),
        ),
        migrations.AddField(
            model_name='saida',
            name='modificado',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='modificado em:'),
        ),
    ]