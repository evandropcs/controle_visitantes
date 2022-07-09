# Generated by Django 3.0 on 2022-07-09 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitante',
            name='data_nascimento',
            field=models.DateField(verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='horario_autorizacao_entrada',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário de autorização de entrada'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='horario_saida',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Horário de saída do condominio'),
        ),
        migrations.AlterField(
            model_name='visitante',
            name='numero_casa',
            field=models.PositiveSmallIntegerField(verbose_name='Número da casa a ser visitada'),
        ),
    ]
