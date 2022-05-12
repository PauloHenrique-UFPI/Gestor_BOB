from django.db import models

class Reseva(models.Model):#classe para tratar dos funcionarios do sistema
    
    usuario = models.ManyToManyField(
        "usuarios.Usuario",
        verbose_name="Usuário",
    )


    
    livro = models.ManyToManyField(
        "livros.Livro",
        verbose_name="Livro",
    )
    
    data = models.DateField(
        verbose_name="Data da Mensagem",
        auto_now_add=True,
    )
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        db_table = "reserva"
        
        def __str__(self):
            return self.usuario