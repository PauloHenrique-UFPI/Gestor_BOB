from django.shortcuts import render
from django.shortcuts import (render, redirect, get_object_or_404)

def home_fun(request):
      
    context = {
        "nome_pagina": "home",
    }
    
    return render(request, "home_fun.html", context)
