"""
URL configuration for template project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from template import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('itens/', views.itens_list, name='itens_list'),
    path('requisicoes/', views.requisicoes_list, name='requisicoes_list'),
    path('solicitar/', views.requisicao_nova, name='requisicao_nova'),
    path('gestao/', views.gestao_dashboard, name='gestao_dashboard'),
    path('relatorios/', views.relatorios, name='relatorios'),
    path('login/', views.user_login, name='login'),
    
]
