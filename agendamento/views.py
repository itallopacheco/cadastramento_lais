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
    a = Agendamento.objects.filter(account=request.user)
    estabelecimentos = Estabelecimento.objects.all().order_by()
    context = {}
    form = AgendamentoForm()

    for ag in a:
        if ag.is_active == True:
            add_message(request, messages.WARNING, 'Não pode ter mais de um agendamento ativo')
            return redirect('home')

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():

            print("FORM VALIDO")
            hora = request.POST.get('horario')
            estabelecimento = form.cleaned_data.get('estabelecimento')
            data_agendamento = form.cleaned_data.get('data_agendamento')
            account = Account.objects.filter(id=user.pk).first()
            if hora not in (HORA_CHOICES):
                msg="Não existem horários disponiveis"
                form.add_error('',msg)

            agendamento = Agendamento.objects.create(estabelecimento= estabelecimento,data_agendamento= data_agendamento,
                                                      hora= hora)
            agendamento.account.add(account.pk)
            print(f"{agendamento}")
            return redirect('home')
        else:
            context={'resgistration_form': form}


    return render(request, 'agendamento/agendamento_form.html', context={'estabelecimentos':estabelecimentos,
                                                                          'registration_form':form})

@login_required(redirect_field_name='home')
def load_horas(request):
    estabelecimento = request.GET.get('estabelecimento')
    data_agendamento = request.GET.get('data_agendamento')
    print(f"LOAD_HORAS {estabelecimento}, {data_agendamento}")
    horario = ()
    agendamentos = Agendamento.objects.filter(estabelecimento=estabelecimento,
                                           data_agendamento=data_agendamento)
    account = Account.objects.filter(id=request.user.id).first()

    horario_ocupado = [(0, 0)]
    if agendamentos.filter(hora='13:00').count() >= 5:
        horario_ocupado.append(time(13, 00, 00))
    if agendamentos.filter(hora='14:00').count() >= 5:
        horario_ocupado.append(time(14, 00, 00))

    if agendamentos.filter(hora='15:00').count() >= 5:
        horario_ocupado.append(time(15, 00, 00))

    if agendamentos.filter(hora='16:00').count() >= 5:
        horario_ocupado.append(time(16, 00, 00))

    if agendamentos.filter(hora='17:00').count() >= 5:
        horario_ocupado.append(time(17, 00, 00))

    horario_permitido = []
    if account.idade in range(18,29,1):
        horario_permitido.append(time(13, 00, 00))
    elif account.idade in range(30,39,1):
        horario_permitido.append(time(14, 00, 00))
    elif account.idade in range(40,49,1):
        horario_permitido.append(time(15, 00, 00))
    elif account.idade in range(50, 59, 1):
        horario_permitido.append(time(16, 00, 00))
    else:
        horario_permitido.append(time(15,00,00))


    horarios_disponiveis = [x for x in HORA_CHOICES if x[0] not in horario_ocupado]
    horario = [x for x in horarios_disponiveis if x[0] in horario_permitido]

    return render(request, 'agendamento/agendamento_choices.html', {'horarios': horario})