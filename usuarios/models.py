from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)



class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):#função para criar o usuario
        usuario = self.model(
            email=self.normalize_email(email)#evita que o email seja salvo com maiusculo caracteres especiais e etc
        )
        
        usuario.is_active = True# explico abaixo
        usuario.is_staff = False# mesmo
        usuario.is_superuser = False#mesmo
        
        if password:#verifica se foi passado uma senha
            usuario.set_password(password)#passa a senha para a função do django
            
        usuario.save()#salva as informações no banco de dados
        
        return usuario
    
    def create_superuser(self, email, password):#semelhante a função anterior
        usuario = self.create_user(#ao invez de criar uma nova função, utiliza a anterior
            email=self.normalize_email(email),
            password=password,
        )
        
        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True
        
        usuario.set_password(password)
        
        usuario.save()
        
        return usuario
        
        

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(#campo para email do usuario
        verbose_name="E-mail do usuário",#apelido para as labels
        max_length=194,#tamanho maximo do campo
        unique=True,#validação para que dois usuario não possam usar o mesmo email
    )
    
    is_active = models.BooleanField(#validação do django para saber se o usuario é ativo no sistema
        verbose_name="Usuário está ativo",#apelido 
        default=True#define que o usuario esta ativo
    )
    
    is_staff = models.BooleanField(#delimita as operações no sistema que usuario pode desempenhar(não queremos que ele tenha acesso a isso)
        verbose_name="Usuário é da equipe de desenvolvimento",#apelido
        default=False,#não queremos que o usuario possa alterar o sistema
    )
    
    is_superuser = models.BooleanField(#define se o usuario é um adm (não queremos que ele seja)
        verbose_name="Usuário é um superusuario",#apelido
        default=False,#esse usuario não pode ser um superusuario
    )
    
    USERNAME_FIELD = "email" #define que o meu metodo de login vai usar apenas o email
    
    objects = UsuarioManager()
    
    class Meta:#classe para os metadados para o django admin
        verbose_name = "Usuário"#apelido
        verbose_name_plural = "Usuários"#apelido para o plural
        db_table = "usuario"#define o banco de dados
        
    def __srt__(self):
        return self.email
     
