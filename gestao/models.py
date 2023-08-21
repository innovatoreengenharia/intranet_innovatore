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
    OPC_SUB =[
        ('finaceiro', '/financeiro/'),
        ('vendas', '/vendas/')
    ]
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='')
    subpasta = models.CharField(max_length=100, choices=OPC_SUB ,blank=False, default='')

    def get_doc_subpasta(instance, filename):
        return f"docs/qualidade/{instance.subpasta}/{filename}"
    doc = models.FileField( upload_to=get_doc_subpasta, blank=True)

    def __str__(self):
        return self.nome
    
