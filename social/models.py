from usuario.models import Perfil
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post/', blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# class Like(models.Model):
#     user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

# class Comment(models.Model):
#     user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
