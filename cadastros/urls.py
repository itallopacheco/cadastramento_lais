"""cadastros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from personal.views import (
    home_view,
    administrativo_view,
    get_data,
    get_data_chart2
)

from account.views import (
    register_view,
    login_view,
    logout_view,
)
from agendamento.views import (
    agendamento_view,
    load_horas,
)


urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('agendamento', agendamento_view, name='agendamento'),
    path('administrativo', administrativo_view, name="adminstrativo"),
    path('administrativo/data', get_data, name="administrativo/data"),
    path('administrativo/data/chart2', get_data_chart2, name="administrativo/data/chart2"),
    path('ajax/load-horas', load_horas, name='ajax_load_horas'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
