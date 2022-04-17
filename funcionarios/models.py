from django.db import models


class Funcionario(models.Model):#classe para tratar dos funcionarios do sistema
    
    usuario = models.OneToOneField(
        "usuarios.Usuario",
        verbose_name="Usuário",
        on_delete=models.PROTECT,
    )
    
    nome_completo = models.CharField(
        verbose_name="Nome do funcionario",#apelido
        max_length=194,#tamanho maximo do campo
    )
    
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )
    
    telefone = models.CharField(
        verbose_name="Telefone de contato",
        max_length=11,
    )
    
    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,#para definir como fixo a data
        auto_now_add=False,#define a data do computador como a data
    )
    
   
    class Meta:
        verbose_name = "Funcionario"
        verbose_name_plural = "Funcionarios"
        db_table = "funcionario"
        
        def __str__(self):
            return self.nome_completo