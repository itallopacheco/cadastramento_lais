from django.contrib import admin
from agendamento.models import Estabelecimento, Agendamento
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
    list_display = ('estabelecimento', 'data_agendamento', 'dia_extenso', 'hora')
    search_fields = ('estabelecimento', 'data_agendamento','hora')
    ordering = ('estabelecimento',)
    filter_horizontal = ()
    fieldsets = ()
