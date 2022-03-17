import dateutil.utils
from django import forms
from django.contrib.auth.forms import UserCreationForm
from dateutil.relativedelta import relativedelta
from cpf_field.forms import CPFFieldForm
from django.utils.datetime_safe import date
from django.contrib.auth import authenticate


from account.models import Account, grupos_atendimento

class RegistrationForm(UserCreationForm):

    nome_completo = forms.CharField(max_length=255, help_text="Insira seu nome completo.")
    cpf = CPFFieldForm()
    data_nascimento = forms.DateField(help_text="Insira sua data de nascimento")
    grupos_atendimento = forms.ModelChoiceField(queryset=grupos_atendimento.objects.all(), label='grupo_atendimento', help_text="grupos de atendimento")
    covid_recente = forms.BooleanField(help_text="Teve covid nos ultimos 30 dias ?", initial=False, required=False)

    class Meta:
        model = Account
        fields = ('nome_completo', 'cpf', 'data_nascimento', 'grupos_atendimento', 'covid_recente', 'password1', 'password2')

    def clean_nome_completo(self):
        nome_completo = self.cleaned_data.get('nome_completo')
        if any(char.isdigit() for char in nome_completo):
            msg = "O nome não pode conter dígitos."
            self.add_error('nome_completo',msg)
        return nome_completo

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        idade = relativedelta(date.today(), data_nascimento).years
        if idade < 18:
            msg ="Você precisa ser maior de 18 anos para se cadastrar no sistema."
            self.add_error('data_nascimento', msg)
        return data_nascimento

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Account.objects.filter(cpf=cpf).exists():
            msg = "O CPF inserido já é cadastrado."
            self.add_error('cpf',msg)
        return cpf

    def clean_covid_recente(self):
        covid_recente = self.cleaned_data.get('covid_recente')
        return covid_recente

class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('cpf', 'password')

    def clean(self):
        if self.is_valid():
            cpf = self.cleaned_data.get('cpf')
            password = self.cleaned_data.get('password')
            if not authenticate(cpf=cpf, password=password):
                msg = "Cpf ou senha invalido"
                self.add_error('cpf', msg)
