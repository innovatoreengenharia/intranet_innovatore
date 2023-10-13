from django.db import models
from datetime import datetime

class Cursos(models.Model):

    class Meta:
        verbose_name_plural = "Cursos"

    imagem = models.ImageField(upload_to="cursos/", blank=True, null=True)
    setor = models.CharField(max_length=100, null=True, blank=True)
    nome =  models.CharField(max_length=150, null=False, blank=False)
    horas = models.CharField(max_length=50, null=True, blank=True)
    data = models.DateTimeField(default=datetime.now, blank=False)