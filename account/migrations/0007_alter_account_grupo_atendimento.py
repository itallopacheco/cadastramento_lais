# Generated by Django 4.0.3 on 2022-03-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_account_grupo_atendimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='grupo_atendimento',
            field=models.ManyToManyField(blank=True, related_name='account', to='account.grupos_atendimento', verbose_name='grupo atendimento'),
        ),
    ]
