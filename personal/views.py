from django.shortcuts import render
from agendamento.models import Agendamento_Account
from django.contrib.auth.decorators import login_required

def home_view(request,*args, **kwargs):
    if(request.user.is_authenticated):
        agendamentos = Agendamento_Account.objects.filter(account=request.user)
        return render(request, "personal/home.html", context = {'agendamentos': agendamentos})

    return render(request,"personal/home.html",context={})