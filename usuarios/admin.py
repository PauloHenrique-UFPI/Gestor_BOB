from django.contrib import admin
from usuarios.models import Usuario

admin.site.register(Usuario)#cria a administração deste modelo no admin do django
