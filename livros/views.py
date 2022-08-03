
from django.shortcuts import (render, redirect, get_object_or_404)


from livros.models import Livro

def acervo(request):
    
    todos_livros = Livro.objects.all()
    
    context = {
        "nome_pagina": "Acervo",
        "todos_livros": todos_livros,
    }
    
    return render(request,'Acervo.html',context)

def home(request):
    
    todos_livros = Livro.objects.all()
    
    context = {
        "nome_pagina": "home",
        "todos_livros": todos_livros,
    }
    
    return render(request, "home.html", context)

def informacoes_livros(request, id):
    
    livro = get_object_or_404(
        Livro,
        id = id
    )
    
    context = {
        "nome_pagina": "Informações do livro",
        "livro": livro,
    }
    
    return render(request, "livro.html", context)



