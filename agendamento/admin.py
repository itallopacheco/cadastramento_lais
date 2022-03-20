from django.contrib import admin
from agendamento.models import Estabelecimento
# Register your models here.

@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_filter = ('cnes', 'nome')
    list_display = ('id', 'cnes', 'nome',)
    search_fields = ('cnes', 'nome',)
    ordering = ('nome',)
    filter_horizontal = ()
    fieldsets = ()
