from django.shortcuts import render
from django.shortcuts import (render, redirect, get_object_or_404)

from reserva.models import Reseva

def reserva(request):
    
    todas_reserva = Reseva.objects.all()
    
    context = {
        "nome_pagina": "reserva",
        "todas_reserva": todas_reserva,
    }
    
    return render(request,'reserva.html',context)

