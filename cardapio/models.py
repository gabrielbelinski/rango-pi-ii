from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    preco = models.FloatField(null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    imagem = models.CharField(max_length=100, null=False, blank=False)
    disponibilidade = models.BooleanField(default=True)
    

    def __str__(self):
        return f"Produto [nome={self.nome}]"

