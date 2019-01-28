from django.shortcuts import render

from django.http import HttpResponse
from Ttemplate.forms import Cadastro

from .models import cadastro
def home(request):
    return render(request,'base.html')

def cadastros(request):
    form = Cadastro(request.POST or None)
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")
    else:
        form= Cadastro()
        return render(request,'cadastro.html',{'form':form})


def lista(request):
    cadastros = cadastro.objects.all()
    context = {'cadastro':cadastros}
    return render(request,'lista_cadastro.html',context)




"""def lista(request):
    cadastros = cadastro.objetos.all()
    context = {'Cadastro':cadastros}
    return render(request,'lista_cadastro.html',context=context)
"""
