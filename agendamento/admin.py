from django.contrib import admin
from agendamento.models import Estabelecimento, Agendamento, Agendamento_Account
# Register your models here.

@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_filter = ('cnes', 'nome')
    list_display = ('id', 'cnes', 'nome',)
    search_fields = ('cnes', 'nome',)
    ordering = ('nome',)
    filter_horizontal = ()
    fieldsets = ()

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_filter = ('estabelecimento', 'data_agendamento', 'account')
    list_display = ('id', 'estabelecimento', 'data_agendamento', 'dia_extenso',)
    search_fields = ('estabelecimento', 'data_agendamento',)
    ordering = ('estabelecimento',)
    filter_horizontal = ()
    fieldsets = ()

@admin.register(Agendamento_Account)
class Agendamento_Account(admin.ModelAdmin):
    list_filter = ('account', 'agendamento', 'hora', 'is_active')
    list_display = ('account', 'agendamento', 'hora', 'is_active', 'status')
    search_fields = ('account',)
    ordering = ('account',)
    filter_horizontal = ()
    fieldsets = ()
