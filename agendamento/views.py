from django.shortcuts import render, redirect
from agendamento.models import Agendamento, Estabelecimento, Agendamento_Account
from django.contrib.auth import authenticate
from agendamento.choices import *
from django.contrib.messages import constants as messages, add_message
from agendamento.forms import AgendamentoForm
from django.contrib.auth.decorators import login_required
from datetime import date



@login_required(redirect_field_name='home')
def agendamento_view(request, *args, **kwargs):
    user = request.user
    a = Agendamento_Account.objects.filter(account=request.user, is_active=True)
    estabelecimentos = Estabelecimento.objects.all()

    horario = HORA_CHOICES
    context = {}

    if a: #checa se a pessoa tem agendamentos ativos
        add_message(request, messages.WARNING, 'Não pode ter mais de um agendamento ativo')
        return redirect('home')

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento')
        else:
            context['registration_form'] = form

    return render(request, 'agendamento/agendamento_form.html', context={'estabelecimentos':estabelecimentos,
                                                                            'horarios': horario})


