from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from account.models import Account, GrupoAtendimento
from django.contrib.messages import constants as messages, add_message


def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return redirect('home')

    objectlist = GrupoAtendimento.objects.all()
    context = {'objectlist': objectlist}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)

            usuario.save()
            form.save_m2m()
            nome_completo = form.cleaned_data.get('nome_completo')
            cpf = form.cleaned_data.get('cpf')
            data_nascimento = form.cleaned_data.get('data_nascimento')
            grupo_atendimento = form.cleaned_data.get('grupos_atendimento')
            covid_recente = form.cleaned_data.get('covid_recente')
            password = form.cleaned_data.get('password1')
            account = authenticate(nome_completo=nome_completo, cpf=cpf, data_nascimento=data_nascimento,
                                   grupos_atendimento=grupo_atendimento,covid_recente=covid_recente,
                                   password=password)
            add_message(request,messages.INFO,"Usuario criado com sucesso!")
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    return render(request, 'account/register.html',context )

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request,*args,**kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            cpf = request.POST['cpf']
            password = request.POST['password']
            user = authenticate(cpf=cpf, password=password)
            if user:
                login(request,user)
                return redirect('home')
        else:
            context['login_form'] = form
    return render(request, "account/login.html", context)
