from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Perfil(models.Model): 
    class Meta:
        verbose_name_plural = "Perfis"
    GEN = [
        ('masculino', 'M'), 
        ('feminino', 'F')
    ]
    ESTADO = [
        ('Acre', 'AC'),
        ('Alagoas',	'AL'),
        ('Amapá', 'AP'),
        ('Amazonas', 'AM'),
        ('Bahia', 'BA'),
        ('Ceará', 'CE'),
        ('Distrito Federal', 'DF'),
        ('Espírito Santo', 'ES'),
        ('Goiás', 'GO'),
        ('Maranhão', 'MA'),
        ('Mato Grosso',	'MT'),
        ('Mato Grosso do Sul', 'MS'),
        ('Minas Gerais', 'MG'),
        ('Pará', 'PA'),
        ('Paraíba', 'PB'),
        ('Paraná', 'PR'),
        ('Pernambuco', 'PE'),
        ('Piauí', 'PI'),
        ('Rio de Janeiro', 'RJ'),
        ('Rio Grande do Norte',	'RN'),
        ('Rio Grande do Sul', 'RS'),
        ('Rondônia', 'RO'),
        ('Roraima',	'RR'),
        ('Santa Catarina', 'SC'),
        ('São Paulo', 'SP'),
        ('Sergipe',	'SE'),
        ('Tocantins', 'TO'),
    ]
    # Informações Basicas 
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to="fotos/", blank=True)
    fundo = models.ImageField(upload_to="fundos/", blank=True)
    nome = models.CharField(max_length=30, null=True)
    sobrenome = models.CharField(max_length=50, null=True)
    nascimento = models.DateField(max_length=10, null=True, blank=True)
    sexo = models.CharField(max_length=20, choices=GEN, null=True, default='M')
    email = models.EmailField(max_length=50,null=True)
    contato = models.CharField(max_length=14)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    rg = models.CharField(max_length=25, null=True, blank=True)
    endereco = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO, null=True, default='AC')
    numero = models.CharField(max_length=15, null=True, blank=True)
    complemento = models.CharField(max_length=30, null=True, blank=True)

    # Informações Profissionais
    cargo_inicial = models.CharField(max_length=50, null=True, blank=True)
    cargo = models.CharField(max_length=50, null=True, blank=True)
    setor = models.CharField(max_length=50, null=True, blank=True)
    cidade_trabalho = models.CharField(max_length=50, null=True, blank=True)
    estado_trabalho = models.CharField(max_length=50, choices=ESTADO, null=True, default='AC')
    data_inicio = models.DateField(max_length=10, null=True, blank=True)
    data_mudanca = models.DateField(max_length=10, null=True, blank=True)
    email_empresa = models.EmailField(max_length=50, null=True, blank=True)
    telefone = models.CharField(max_length=30, null=True, blank=True)
    obra_trabalho = models.CharField(max_length=50, null=True, blank=True)
    texto_experiencia = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.nome
    

# Experiência Profissional
class Experiencia(models.Model):
    class Meta:
        verbose_name_plural = "Experiências"

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)

    empresa = models.CharField(max_length=50, null=True, blank=True)
    cargo_empresa = models.CharField(max_length=70, null=True, blank=True)
    localidade = models.CharField(max_length=50, null=True)
    forma_trabalho = models.CharField(max_length=50, null=True)
    inicio_trabalho = models.DateField(max_length=10, null=True, blank=True)
    termino_trabalho = models.DateField(max_length=10, null=True, blank=True)
    descricao_trabalho = models.TextField(null=True, blank=True)


# Formação Acadêmica
class Formacao(models.Model):
    class Meta:
        verbose_name_plural = "Formações"

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)

    instituicao = models.CharField(max_length=50, null=True)
    diploma = models.CharField(max_length=50, null=True, blank=True)
    area_estudo = models.CharField(max_length=60, null=True, blank=True)
    inicio_faculdade = models.DateField(max_length=10, null=True, blank=True)
    termino_faculdade= models.DateField(max_length=10, null=True, blank=True)
    descricao_faculdade = models.TextField(null=True, blank=True)


# Licenças ou Cursos
class Cursos(models.Model):
    class Meta:
        verbose_name_plural = "Cursos"

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)

    nome_certificado = models.CharField(max_length=50, null=True)
    organizacao = models.CharField(max_length=50, null=True)
    inicio_curso = models.DateField(max_length=10, null=True,blank=True)
    termino_curso= models.DateField(max_length=10, null=True, blank=True)
    horas = models.CharField(max_length=30, null=True)
    descricao_curso = models.TextField(null=True, blank=True)


# Habilidades
class Habilidades(models.Model):
    class Meta:
        verbose_name_plural = "Habilidades"
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    habilidades = models.CharField(max_length=50, null=True)

# Hobbies
class Hobbies(models.Model):
    class Meta:
        verbose_name_plural = "Hobbies"
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)
    hobbies = models.CharField(max_length=50, null=True)


    





