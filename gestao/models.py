from django.db import models
from datetime import datetime

class Qualidade(models.Model):
    class Meta:
        verbose_name_plural = "Qualidade"
    OPC_DOC = [
        ('PDF','pdf'),
        ('TXT','txt'),
        ('XLS','xls'),
        ('DOC','doc'),
        ('PPT', 'ppt')

    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    doc = models.FileField( upload_to="docs/qualidade/%Y/%m/", blank=True)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='')

    def __str__(self):
        return self.nome
    
