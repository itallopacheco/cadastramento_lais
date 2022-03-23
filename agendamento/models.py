from django.db import models
from account.models import Account
from datetime import date
from django.utils.timezone import localtime
from agendamento.choices import *
from django.core.validators import MinValueValidator
# Create your models here.

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome do estabelecimento')
    cnes = models.CharField(max_length=50, verbose_name='Código CNES')
    logradouro = models.CharField(max_length=255, verbose_name='Logradouro')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, verbose_name='Estabelecimento')
    data_agendamento = models.DateField(verbose_name='Data Agendamento',validators=[MinValueValidator(limit_value=date.today())])
    account = models.ManyToManyField(Account)
    hora = models.TimeField(auto_now=False, auto_now_add=False, default='00:00', verbose_name='Hora do agendamento',
                            choices=HORA_CHOICES,
                            )
    def __str__(self):
        return f"{self.estabelecimento.nome}, {self.data_agendamento}, {self.dia_extenso}"

    @property
    def dia_extenso(self):
        dias_semana = {0: 'Segunda-Feira',
                       1: 'Terça-Feira',
                       2: 'Quarta-Feira',
                       3: 'Quinta-Feira',
                       4: 'Sexta-Feira',
                       5: 'Sábado',
                       6: 'Domingo'}

        agendamento = dias_semana[self.data_agendamento.weekday()]
        return agendamento

    @property
    def status(self):
        data_agendamento = self.data_agendamento
        if date.today() == data_agendamento and localtime().time() > self.hora:
            return 'Encerrado'
        else:
            if date.today() > data_agendamento:
                return 'Encerrado'
        return 'Ativo'

    @property
    def is_active(self):
        data_agendamento = self.data_agendamento
        hora_agendamento = self.hora
        if date.today() > data_agendamento:
            return False
        elif date.today() == data_agendamento and hora_agendamento < localtime().time():
            return False
        else:
            return True