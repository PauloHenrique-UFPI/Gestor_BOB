from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    context = {
        "nome_pagina": "LOGIN",
    }
    
    return render(request, "index.html", context)

def sobre(request):
    
    context = {
        "nome_pagina": "sobre",
    }
    
    return render(request, "sobre.html", context)
    
def contato(request):
        
    context = {
        "nome_pagina": "contato",
    }
    
    return render(request, "contato.html", context)
    