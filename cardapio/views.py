from django.shortcuts import render

from cardapio.models import Produto

# Create your views here.

produtos = {}
def index(request):
    return render(request, 'cardapio/index.html')

def exibeProdutos(request):
    produtos = Produto.objects.all()
    return render(request, 'cardapio/index.html', {'produtos':produtos})


