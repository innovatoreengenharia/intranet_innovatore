from usuario.models import Perfil
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post/', blank=True)
    texto_postagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

class Comentarios(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto_comentario = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)


# class Like(models.Model):
#     user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)