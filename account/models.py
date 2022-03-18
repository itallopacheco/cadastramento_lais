from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from cpf_field.models import CPFField
from datetime import date

# Create your models here.

class AccountManager(BaseUserManager):

    def create_user(self, nome_completo, cpf, data_nascimento, grupo_atendimento,covid_recente, password=None):
        if not cpf:
            raise ValueError("Usuarios precisam ter um cpf.")
        if not nome_completo:
            raise ValueError("Usuarios precisam ter um nome.")
        user = self.model(
                nome_completo = nome_completo,
                cpf = cpf,
                data_nascimento = data_nascimento,
                grupo_atendimento =grupo_atendimento,
                covid_recente = covid_recente
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nome_completo, cpf, data_nascimento, covid_recente, password=None):
        user = self.model(
            nome_completo=nome_completo,
            cpf=cpf,
            data_nascimento =data_nascimento,
            covid_recente = covid_recente
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class GrupoAtendimento(models.Model):
    nome = models.CharField(max_length=150, verbose_name="nome grupo atendimento")
    visivel = models.BooleanField(default=True, blank=True,null=True, verbose_name="visibilidade")
    fase = models.CharField(max_length=15, blank=True, null=True, default="000")
    codigo_si_pni = models.CharField(max_length=15,blank=True,null=True)
    grupo_pai = models.CharField(max_length=5,blank=True,null=True)
    criado_em = models.DateTimeField(auto_now_add=True,verbose_name="data de criacao")
    atualizado_em = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.nome


class Account(AbstractBaseUser):

    nome_completo                   = models.CharField(max_length=150, verbose_name="nome completo")
    cpf                             = CPFField(unique=True, verbose_name='cpf',)
    data_nascimento                 = models.DateField(verbose_name="data de nascimento")
    grupos_atendimento              = models.ManyToManyField(GrupoAtendimento, related_name='account', blank=True, verbose_name="grupo atendimento")
    covid_recente                   = models.BooleanField(verbose_name="teve covid recentemente")
    date_joined                     = models.DateTimeField(verbose_name="data de cadastro", auto_now_add=True)
    is_admin                        = models.BooleanField(default=False)
    is_active                       = models.BooleanField(default=True)
    is_staff                        = models.BooleanField(default=False)
    is_superuser                    = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['nome_completo', 'data_nascimento', 'covid_recente']

    def __str__(self):
        return self.nome_completo

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def idade(self):
        today = date.today()
        return today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
    @property
    def get_grupos_sipni(self):
        return "\n".join([a.codigo_si_pni for a in self.grupos_atendimento.all()])

    @property
    def get_grupos(self):
        return "\n".join([a.nome for a in self.grupos_atendimento.all()])

    @property
    def able_to_schedule(self):
        return self.get_grupos_sipni not in ['001101', '000205', '001501'] and self.idade > 18 and not self.covid_recente