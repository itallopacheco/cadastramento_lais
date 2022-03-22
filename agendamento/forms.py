from django import forms
from django.utils.datetime_safe import date
from agendamento.choices import *
from agendamento.models import Agendamento, Estabelecimento
from cadastros.settings import DATE_INPUT_FORMATS


class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = Agendamento
        fields = ['estabelecimento', 'data_agendamento']
