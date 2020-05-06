from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from core.models import Produto


def index(request):
    # produtos = Produto.objects.all()
    produtos = get_list_or_404(Produto)
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def produto(request, pk: int):
    # prod = Produto.objects.filter(id=pk).first()
    try:
        prod = get_object_or_404(Produto, id=pk)
    except Exception:
        raise Http404("No MyModel matches the given query.")
        # return redirect('index')
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)


def contato(request):
    return render(request, 'contato.html')


def error404(request, exception):
    return render(request, 'error404.html')
