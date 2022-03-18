# Generated by Django 4.0.3 on 2022-03-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_grupos_atendimento_visivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='grupo_atendimento',
        ),
        migrations.AddField(
            model_name='account',
            name='grupo_atendimento',
            field=models.ManyToManyField(blank=True, to='account.grupos_atendimento', verbose_name='grupo atendimento'),
        ),
        migrations.AlterField(
            model_name='grupos_atendimento',
            name='visivel',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='visibilidade'),
        ),
    ]
