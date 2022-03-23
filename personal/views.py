from django.http import JsonResponse
from django.shortcuts import render, redirect
from agendamento.models import Agendamento,Estabelecimento
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def home_view(request,*args, **kwargs):
    if(request.user.is_authenticated):
        agendamentos = Agendamento.objects.filter(account=request.user)
        return render(request, "personal/home.html", context = {'agendamentos': agendamentos})

    return render(request,"personal/home.html",context={})


@login_required(redirect_field_name='home')
def administrativo_view(request,*args,**kwargs):
    if request.user.is_superuser:
        return render(request, "personal/painel_administrativo.html", context={})
    else:
        return redirect('home')


@login_required(redirect_field_name='home')
def get_data(request,*args,**kwargs):
    if request.user.is_superuser:
        queryset = Agendamento.objects.order_by('account__agendamento__estabelecimento_id').values('account__agendamento__estabelecimento_id').annotate(estab_count = Count('estabelecimento_id'))

        data = list(queryset.values_list('estab_count', flat=True))
        labels = ['aptos', 'inaptos']

        data = {
                'labels': labels,
                'data': data,
                }
        return JsonResponse(data)
    else:
        return redirect('home')


@login_required(redirect_field_name='home')
def get_data_chart2(request, *args, **kwargs):
    if request.user.is_superuser:
        count_able =0
        count_inable = 0
        inaptos = Account.objects.all()
        for i in inaptos:
            if i.able_to_schedule:
                count_able += 1
            else:
                count_inable += 1

        print(count_able)
        print(count_inable)
        data = [count_able,count_inable]
        data = {
            'data': data

        }

        return JsonResponse(data)
    else:
        return redirect('home')