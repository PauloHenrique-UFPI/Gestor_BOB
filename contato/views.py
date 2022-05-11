from django.shortcuts import render
from django.shortcuts import (render, redirect, get_object_or_404)

from contato.models import Contato

def lcontatos(request):
    
    todos_contatos = Contato.objects.all()
    
    context = {
        "nome_pagina": "lcontatos",
        "todos_contatos": todos_contatos,
    }
    
    
    return render(request,'lcontatos.html',context)

