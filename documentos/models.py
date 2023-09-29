from django.db import models
from datetime import datetime

OPC_DOC = [
    ('PDF','pdf'),
    ('TXT','txt'),
    ('XLS','xls'),
    ('DOC','doc'),
    ('PPT', 'ppt')

]

class Comercial(models.Model):
    class Meta:
        verbose_name_plural = "Comercial"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome
    
class Controladoria(models.Model):
    class Meta:
        verbose_name_plural = "Controladoria"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class DepartamentoPessoal(models.Model):
    class Meta:
        verbose_name_plural = "Departamento Pessoal"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Engenharia(models.Model):
    class Meta:
        verbose_name_plural = "Engenharia"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Financeiro(models.Model):
    class Meta:
        verbose_name_plural = "Financeiro"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Qualidade(models.Model):
    class Meta:
        verbose_name_plural = "Qualidade"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Fiscal(models.Model):
    class Meta:
        verbose_name_plural = "Fiscal"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Juridico(models.Model):
    class Meta:
        verbose_name_plural = "Jurídico"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Logistica(models.Model):
    class Meta:
        verbose_name_plural = "Logística"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Marketing(models.Model):
    class Meta:
        verbose_name_plural = "Marketing"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class MeioAmbiente(models.Model):
    class Meta:
        verbose_name_plural = "Meio Ambiente"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Orcamentos(models.Model):
    class Meta:
        verbose_name_plural = "Orçamentos"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class PMO(models.Model):
    class Meta:
        verbose_name_plural = "P.M.O."
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Qualidade(models.Model):
    class Meta:
        verbose_name_plural = "Qualidade"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class RecursosHumanos(models.Model):
    class Meta:
        verbose_name_plural = "Recursos Humanos"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class SegurancaDoTrabalho(models.Model):
    class Meta:
        verbose_name_plural = "Segurança do Trabalho"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Sistemas(models.Model):
    class Meta:
        verbose_name_plural = "Sistemas"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Suprimentos(models.Model):
    class Meta:
        verbose_name_plural = "Suprimentos"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class TI(models.Model):
    class Meta:
        verbose_name_plural = "T.I."
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

class Vendas(models.Model):
    class Meta:
        verbose_name_plural = "Vendas"
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificado = models.DateTimeField(default=datetime.now, blank=False)
    tipo = models.CharField(max_length=150,choices= OPC_DOC, default='PDF')
    doc = models.FileField(upload_to="qualidade/", blank=True)

    def __str__(self):
        return self.nome

