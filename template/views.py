from django.shortcuts import render
from django.http import HttpResponse # Importe o HttpResponse para as placeholders

def home_view(request):
    return render(request, 'index.html', {})

# FUNÇÕES PLACEHOLDERS PARA RESOLVER O NoReverseMatch

def itens_list(request):
    # Por enquanto, retorna apenas um texto simples ou um template de lista de itens
    return HttpResponse("Página de Lista de Itens (A Ser Implementada)")

def requisicoes_list(request):
    return HttpResponse("Página de Requisições (A Ser Implementada)")

def requisicao_nova(request):
    return HttpResponse("Página de Nova Requisição (A Ser Implementada)")
    
def gestao_dashboard(request):
    return HttpResponse("Página de Gestão / Dashboard (A Ser Implementada)")

def relatorios(request):
    return HttpResponse("Página de Relatórios (A Ser Implementada)")

# Use a view padrão do Django para login ou crie uma simples
def user_login(request):
    return HttpResponse("Página de Login (A Ser Implementada)")

# Lembre-se de que, se você estiver usando o DRF,
# estas views serão substituídas por classes de ViewSet.