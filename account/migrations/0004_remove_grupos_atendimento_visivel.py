# Generated by Django 4.0.3 on 2022-03-16 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_grupo_atend_grupos_atendimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupos_atendimento',
            name='visivel',
        ),
    ]
