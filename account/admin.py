from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import Account, GrupoAtendimento
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('nome_completo', 'cpf', 'get_grupos_sipni', 'covid_recente', 'date_joined', 'is_admin', 'is_staff')
    search_fields = ('cpf', 'nome_completo','grupos_atendimento')
    readonly_fields = ('id', 'date_joined',)

    ordering = ('cpf',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None,{
            'classes': ('wide'),
            'fields':  ('nome_completo','cpf','grupos_atendimento','covid_recente','data_nascimento','password1','password2'),
        }),
    )

admin.site.register(Account, AccountAdmin)

@admin.register(GrupoAtendimento)
class GrupoAtendimento(admin.ModelAdmin):
    list_filter = ('nome',)
    list_display = ('nome', 'id')
    search_fields = ('nome',)
    ordering = ('nome',)
    filter_horizontal = ()
    fieldsets = ()