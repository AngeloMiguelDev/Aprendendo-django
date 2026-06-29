from django.shortcuts import render
from django.http import HttpResponse

def produto(request):
    if request.method == "GET":
        nome = 'Ângelo'
        return render(request, 'produto.html', {'nome' : nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        print(nome)
        print(idade)
        return HttpResponse('Fui chamado')

def ver_home(request):
    return HttpResponse('Olá, tudo bem?')