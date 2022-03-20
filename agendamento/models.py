from django.db import models

# Create your models here.

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do estabelecimento')
    cnes = models.CharField(max_length=50, verbose_name='Código CNES')
    logradouro = models.CharField(max_length=255, verbose_name='Logradouro')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')

    def __str__(self):
        return self.nome