from django import forms
from django.shortcuts import render
from django.shortcuts import (render, redirect, get_object_or_404)
from contato.forms import ContatoForm

from contato.models import Contato

def contato(request):
    
    if request.method == "GET":
        form = ContatoForm()
          
        context = {
            "nome_pagina": "contato",
            "form": form
        }
        
        return render(request, "contato.html", context)
    else:
        
        form = ContatoForm(request.POST)
        
        if form.is_valid():
            Contato = form.save()
            form = ContatoForm()
            
        context = {
        "nome_pagina": "contato",
        "form": form
        }
        return render(request, "contato.html", context)
        

def lcontatos(request):
    
    todos_contatos = Contato.objects.all()
    
    context = {
        "nome_pagina": "lcontatos",
        "todos_contatos": todos_contatos,
    }
    
    
    return render(request,'lcontatos.html',context)


