from django.db import models
from account.models import Account
from datetime import date
from django.utils.timezone import localtime
from agendamento.choices import *
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
    data_agendamento = models.DateField(verbose_name='Data Agendamento',)
    account = models.ManyToManyField(Account, through='Agendamento_Account')

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


class Agendamento_Account(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    hora = models.TimeField(auto_now=False, auto_now_add=False,default='00:00', verbose_name='Hora do agendamento',
                            choices=HORA_CHOICES,
                            )
    is_active = models.BooleanField(verbose_name='esta ativo', default=False, null=False)

    @property
    def status(self):
        data_agendamento = self.agendamento.data_agendamento
        if date.today() == data_agendamento and localtime().time() > self.hora:
            self.is_active = False
            return 'Encerrado'
        else:
            if date.today() > data_agendamento:
                self.is_active = False
                return 'Encerrado'
        self.is_active = True
        return 'Ativo'

    @property
    def dia_extenso(self):

        dias_semana = {0: 'Segunda-Feira',
                       1: 'Terça-Feira',
                       2: 'Quarta-Feira',
                       3: 'Quinta-Feira',
                       4: 'Sexta-Feira',
                       5: 'Sábado',
                       6: 'Domingo'}

        agendamento = dias_semana[self.agendamento.data_agendamento.weekday()]
        return agendamento
