from typing import List

from django.shortcuts import render, redirect
from agendamento.models import Agendamento, Estabelecimento
from account.models import Account
from django.contrib.auth import authenticate
from agendamento.choices import *
from django.contrib.messages import constants as messages, add_message
from agendamento.forms import AgendamentoForm
from django.contrib.auth.decorators import login_required
from datetime import date, time
from django.db.models import Count


@login_required(redirect_field_name='home')
def agendamento_view(request, *args, **kwargs):
    user = request.user
    a = Agendamento.objects.filter(account=request.user, is_active=True)
    estabelecimentos = Estabelecimento.objects.all().order_by()

    horario = ()
    context = {}

    if a: #checa se a pessoa tem agendamentos ativos
        add_message(request, messages.WARNING, 'Não pode ter mais de um agendamento ativo')
        return redirect('home')

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():

            estabelecimento = form.cleaned_data.get('estabelecimento')
            data_agendamento = form.cleaned_data.get('data_agendamento')
            print(estabelecimento)
            print(f"{data_agendamento}\n")

            f = Agendamento.objects.filter(estabelecimento=estabelecimento,
                                           data_agendamento=data_agendamento)


            horario_ocupado=[(0,0)]
            if f.filter(hora='13:00').count() >= 5:
                horario_ocupado.append(time(13,00,00))
            if f.filter(hora='14:00').count() >= 5:
                horario_ocupado.append(time(14,00,00))

            if f.filter(hora='15:00').count() >= 5:
                horario_ocupado.append(time(15,00,00))

            if f.filter(hora='16:00').count() >= 5:
                horario_ocupado.append(time(16,00,00))

            if f.filter(hora='17:00').count() >= 5:
                horario_ocupado.append(time(17,00,00))

            horario = [x for x in HORA_CHOICES if x[0] not in horario_ocupado]

            for h in horario:
                print(h)

        else:
           context['registration_form'] = form

    return render(request, 'agendamento/agendamento_form.html', context={'estabelecimentos':estabelecimentos,
                                                                            'horarios': horario})


