# Sistema para Agendamento de Testes de Covid-19
Projeto desenvolvido em **Django** para a segunda fase da seleção de pesquisadores (perfil Back-end) para o Laboratório de Inovação Tecnológica em Saúde (LAIS) **[EDITAL Nº 010/2022](https://lais.huol.ufrn.br/wp-content/uploads/2022/03/Edital-10_2022-Orientacoes-para-a-Fase-2.pdf)**


# Instalação

 - **Clone** e acesse o repositório no seu terminal.

> `git clone https://github.com/itallopacheco/cadastramento_lais.git`
 - **Crie** um **[venv](https://docs.python.org/pt-br/3/library/venv.html)** com:
> `python -m venv venv` e ative a venv com `venv/scripts/activate`
- Já **dentro da venv** instale os requisitos da aplicação com:
> `pip install -r requirements.txt`
- Em cadastros/settings.py **procure** por databases e **configure** o banco de dados a sua escolha
- **[Aqui](https://docs.djangoproject.com/en/4.0/ref/settings/#databases)** você pode ver mais sobre configurações de banco.
- Faça as **migrations** com os comandos:
> `python manage.py makemigrations`
> `python manage.py migrate`
- **Carregue** as **[Fixtures](https://docs.djangoproject.com/en/2.0/howto/initial-data/)** para inserir os grupos de atendimento no **[xml](https://selecoes.lais.huol.ufrn.br/media/grupos_atendimento.xml)** fornecido pelas instruções do projeto
> ``python ./manage.py loaddata grupos_atendimento.json``

- **Utilize** o comando abaixo para inserir os estabelecimentos.
> ``python ./manage.py inserir_estabelecimentos``

- **Crie** um SuperUser com o seguinte comando:
> ``python ./manage.py createsuperuser``
> Detalhe, a data de nascimento é inserida no formato **YY-MM-DD**
> O campo teve covid nos ultimos 30 dias deve ser respondido com **0** para **não** e **1** para **sim**

- Agora **inicie** o servidor local.
> `python manage.py runserver`

- **Acesse** a página de Administração do Django com: 
> `127.0.0.1:8000/admin/`

# APPS

 - Personal
	 - Homepage
	 - Painel Administrativo
- Account
	 - Login
	 - Cadastro
	 - Logout
- Agendamento
	 - Carrega as Horas disponíveis
	 - Realiza o Agendamento
	

