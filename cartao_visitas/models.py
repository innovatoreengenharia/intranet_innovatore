from django.db import models

class Cartao_visitas(models.Model):
    class Meta:
        verbose_name_plural = "Cartões de Visitas"
    nome = models.CharField(max_length=100, null=True, blank=True)
    empresa = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefone_fixo = models.CharField(max_length=100, null=True, blank=True)
    telefone_celular = models.CharField(max_length=100, null=True, blank=True)
    site = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome