from django import forms
from django.utils.datetime_safe import date
from django.contrib.auth import authenticate
from agendamento.choices import *
from agendamento.models import Agendamento,Agendamento_Account, Estabelecimento


class AgendamentoForm(forms.ModelForm):
    estabelecimento = forms.ModelChoiceField(queryset=Estabelecimento.objects.all().order_by('nome'))
    data_agendamento = forms.DateField()
    hora = forms.ChoiceField(choices=HORA_CHOICES, required=True, help_text="horario do agendamento",)

    class Meta:
        model = Agendamento
        fields = ('estabelecimento', 'data_agendamento', 'hora')
'''
    def clean_data_agendamento(self):
        data_agendamento = self.cleaned_data.get('data_agendamento')
        data_hoje = date.today()
        if data_hoje > data_agendamento:
            msg = "Selecione uma data a partir de hoje"
            self.add_error('data_agendamento', msg)
        if data_agendamento.weekday() == 0 or data_agendamento.weekday() == 1 or data_agendamento.weekday() == 2:
            msg2 = "Só é possível marcar exames de quarta-feira ao sábado"
            self.add_error('data_agendamento', msg2)
        return data_agendamento
'''