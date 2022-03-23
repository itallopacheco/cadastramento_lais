from django import forms
from django.utils.datetime_safe import date
from agendamento.choices import *
from agendamento.models import Agendamento, Estabelecimento
from account.models import Account
from django.core.validators import MinValueValidator
from cadastros.settings import DATE_INPUT_FORMATS


class AgendamentoForm(forms.ModelForm):

    estabelecimento = forms.ModelChoiceField(queryset=Estabelecimento.objects.all().order_by('nome'), help_text="Insira seu nome completo.")
    data_agendamento = forms.DateField( validators=[MinValueValidator(limit_value=date.today())], help_text="Insira a data do seu agendamento")




    class Meta:
        model = Agendamento
        fields = ['estabelecimento', 'data_agendamento']




    def clean_data_agendamento(self):
        datas_proibidas = [0,1,6]
        data_agendamento = self.cleaned_data.get('data_agendamento')
        data_hoje = date.today()
        if data_agendamento < data_hoje:
            msg1 = "Não é possível agendar para datas passadas"
            self.add_error('data_agendamento',msg1)
        if data_agendamento.weekday() in datas_proibidas:
            msg2 = "Não é possível agendar para domingo, segunda ou terça"
            self.add_error('data_agendamento',msg2)

        return data_agendamento


