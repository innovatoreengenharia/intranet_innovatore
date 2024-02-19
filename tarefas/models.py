from usuario.models import Perfil
from django.db import models

class Quadros(models.Model):
    class Meta:
        verbose_name_plural = "Quadros"

    titulo = models.CharField(max_length=50, null=True)
    usuario = models.ManyToManyField(Perfil)

class Colunas(models.Model):
    class Meta:
        verbose_name_plural = "Colunas"

    titulo = models.CharField(max_length=50, null=True)
    quadro = models.ForeignKey(Quadros, on_delete=models.CASCADE)

class Tarefas(models.Model):
    class Meta:
        verbose_name_plural = "Tarefas"
        
    titulo = models.CharField(max_length=50, null=True)
    coluna = models.ForeignKey(Colunas, on_delete=models.CASCADE)