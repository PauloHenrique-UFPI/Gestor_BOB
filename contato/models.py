
from django.db import models

class Contato(models.Model):
    
    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=194,
    ) 
    
    email = models.EmailField(#campo para email do usuario
        verbose_name="E-mail do usuário",#apelido para as labels
        max_length=194,#tamanho maximo do campo
        unique=True,#validação para que dois usuario não possam usar o mesmo email
    )
    
    telefone = models.CharField(
        verbose_name="Numero de Telefone",
        max_length=11,
    )
    
    motivo = models.CharField(
        verbose_name="Motivo da mensagem",
        max_length=150,
    )
    
    mensagem = models.CharField(
        verbose_name="Mensagem",
        max_length=100,
    )
    
    data = models.DateField(
        verbose_name="Data da Mensagem",
        auto_now_add=True,
    )
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        db_table = "contato"
        
    def __str__(self):
        return self.nome_completo
        
        