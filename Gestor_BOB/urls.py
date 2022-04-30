"""Gestor_BOB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from usuarios.views import index
from usuarios.views import sobre
from usuarios.views import contato
from livros.views import home
from livros.views import acervo
from livros.views import informacoes_livros

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path(
        "",
        index,
        name="index",
    ),
    
    path(
        "acervo/",
        acervo,
        name='acervo',
    ),
    
    path(
        "home/",
        home,
        name='home',
    ),
    
    path(
        "sobre/",
        sobre,
        name='sobre',
    ),
    
    path(
        "contato/",
        contato,
        name='contato',
    ), 
    
    path(
        "livro/<int:id>/",
        informacoes_livros,
        name='informacoes_livros',
    )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
