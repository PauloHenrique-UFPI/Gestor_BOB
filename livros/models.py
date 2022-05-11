from email.mime import image
from pydoc import describe
from pyexpat import model
from tabnanny import verbose
from django.db import models

class Livro(models.Model):    
   
    titulo = models.CharField(
        verbose_name= 'Titulo do livro',
        max_length=120,
        unique=True,#validação para que dois usuario não possam usar o mesmo email
    )
    
    nome_autor = models.CharField(
        verbose_name= 'Autor do livro',
        max_length=194
    )
    
    imagem_capa = models.ImageField(
        verbose_name= 'Imagem de capa do livro',
        null = True,
        blank = True
    )
    
    ano_publicacao = models.DateField(
        verbose_name= 'Ano de publicação',
        auto_now=False,#para definir como fixo a data
        auto_now_add=False,#define a data do computador como a data
    )
    
    genero = models.CharField(
        verbose_name='Gênero literário',
        max_length=60
    )
    
    descricao = models.TextField(
        verbose_name= 'Resenha do livro',
        max_length=250
    )
    
    numero_exemplares = models.PositiveSmallIntegerField(
        verbose_name='Quantidade de exemplares disponiveis'
    )
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        db_table = 'livro'
        
    def __str__(self):
        return self.titulo