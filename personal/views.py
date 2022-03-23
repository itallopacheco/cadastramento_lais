from django.http import JsonResponse
from django.shortcuts import render
from agendamento.models import Agendamento,Estabelecimento
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def home_view(request,*args, **kwargs):
    if(request.user.is_authenticated):
        agendamentos = Agendamento.objects.filter(account=request.user)
        return render(request, "personal/home.html", context = {'agendamentos': agendamentos})

    return render(request,"personal/home.html",context={})

def administrativo_view(request,*args,**kwargs):



    return render(request, "personal/painel_administrativo.html", context={})

def get_data(request,*args,**kwargs):
    queryset = Agendamento.objects.order_by('account__agendamento__estabelecimento_id').values('account__agendamento__estabelecimento_id').annotate(estab_count = Count('estabelecimento_id'))


    data = list(queryset.values_list('estab_count', flat=True))
    labels = list(queryset.values_list('estabelecimento_id', flat=True))

    data = {
            'labels': labels,
            'data': data,
            }
    return JsonResponse(data)