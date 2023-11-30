from django.shortcuts import render

from cardapio.models import Produto

# Create your views here.

produtos = {}
def index(request):
    return render(request, 'cardapio/index.html')

def login(request):
    return render(request, 'cardapio/home/home.html')

def exibeProdutos(request):
    produtos = Produto.objects.all()
    return render(request, 'cardapio/index.html', {'produtos':produtos})


