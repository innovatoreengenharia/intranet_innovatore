from django.db import models
from datetime import datetime


class Noticia(models.Model):
    class Meta:
        verbose_name_plural = "Notícias"

    imagem = models.ImageField(upload_to="informativos/imagem", blank=True, null=True)
    imagem_destaque = models.FileField(
        upload_to="informativos/imagem_destaque", blank=True, null=True
    )
    imagem_thumb = models.FileField(
        upload_to="informativos/imagem_thumb", blank=True, null=True
    )
    imagem_noticia = models.FileField(
        upload_to="informativos/imagem_noticia", blank=True, null=True
    )
    titulo = models.CharField(max_length=255, null=False, blank=False)
    paragrafo = models.TextField(null=True, blank=True)
    destaque = models.BooleanField(default=False)
    publicado_em = models.DateTimeField(default=datetime.now, blank=False)

    tags = models.CharField(max_length=255, blank=True, null=True)

    def obter_lista_de_tags(self):
        if self.tags:
            return [tag.strip() for tag in self.tags.split(",")]

    def __str__(self):
        return self.titulo


class Bloco(models.Model):
    class Meta:
        verbose_name_plural = "Blocos"

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, null=True)

    imagem_bloco = models.ImageField(
        upload_to="informativos/imagem_bloco", blank=True, null=True
    )
    titulo_bloco = models.CharField(max_length=255, null=True, blank=True)
    paragrafo_bloco = models.TextField(null=True, blank=True)


class Comunicado(models.Model):
    titulo = models.CharField(max_length=255, null=True, blank=True)
    paragrafo = models.TextField(null=True, blank=True)
    publicado_em = models.DateTimeField(default=datetime.now, blank=False)
