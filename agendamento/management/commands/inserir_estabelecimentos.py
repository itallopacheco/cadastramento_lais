from django.core.management.base import BaseCommand
from agendamento.models import Estabelecimento
from xml import sax
import xml.etree.ElementTree as et



class Command(BaseCommand):


    def handle(self, *args, **options):
        tree = et.parse('estabelecimentos_pr.xml')
        root = tree.getroot()


        for estabelecimento in root.findall('*'):
            nome = estabelecimento.find('no_fantasia').text
            cnes = estabelecimento.find('co_cnes').text
            logradouro = estabelecimento.find('no_logradouro').text
            bairro = estabelecimento.find('no_bairro').text

            estabelecimento =Estabelecimento.objects.create(nome=nome, cnes=cnes, logradouro=logradouro, bairro=bairro)
            print(f"Estabelecimento {nome}, {cnes} inserido com sucesso")