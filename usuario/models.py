from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Perfil(models.Model): 
    GEN = [
        ('masculino', 'MASCILINO'), 
        ('feminino', 'FEMININO')
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
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    foto = models.ImageField(upload_to="fotos", blank=True)
    fundo = models.ImageField(upload_to="fundos", blank=True)
    nome = models.CharField(max_length=20, null=True)
    sobrenome = models.CharField(max_length=50, null=True, blank=True)
    nascimento = models.DateField(default=datetime.now, null=True)
    sexo = models.CharField(max_length=20, choices=GEN, null=True)
    email = models.EmailField(max_length=50,null=True)
    contato = models.CharField(max_length=16)
    cpf = models.CharField(max_length=14, null=True)
    rg = models.CharField(max_length=25, null=True)
    endereco = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=30, null=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=30, choices=ESTADO, null=True)
    numero = models.CharField(max_length=15, null=True)
    complemento = models.CharField(max_length=30, null=True, blank=True)

    # Informações Profissionais
    cargo_inicial = models.CharField(max_length=30, null=True)
    cargo = models.CharField(max_length=30, null=True)
    setor = models.CharField(max_length=30, null=True)
    cidade_trabalho = models.CharField(max_length=30, null=True)
    estado_trabalho = models.CharField(max_length=30, null=True)
    data_inicio = models.DateField(default=datetime.now, null=True)
    data_mudanca = models.DateField(default=datetime.now, null=True)
    email_empresa = models.EmailField(max_length=30, null=True)
    telefone = models.CharField(max_length=30, null=True)
    obra_trabalho = models.CharField(max_length=30, null=True)
    texto_experiencia = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome
    

# Experiência Profissional
class Experiencia(models.Model):

    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, null=True)

    empresa = models.CharField(max_length=30, null=True)
    localidade = models.CharField(max_length=30, null=True)
    forma_trabalho = models.CharField(max_length=30, null=True)
    inicio_trabalho = models.DateField(default=datetime.now, null=True)
    termino_trabalho = models.DateField(default=datetime.now, null=True)
    descricao_trabalho = models.TextField(null=True, blank=True)


# Formação Acadêmica
class Formacao(models.Model):
    instituicao = models.CharField(max_length=30, null=True)
    diploma = models.CharField(max_length=30, null=True)
    area_estudo = models.CharField(max_length=30, null=True)
    inicio_faculdade = models.DateField(default=datetime.now, null=True)
    termino_faculdade= models.DateField(default=datetime.now, null=True)
    descricao_faculdade = models.TextField(null=True, blank=True)


# Licenças ou Cursos
class Cursos(models.Model):
    nome_certificado = models.CharField(max_length=30, null=True)
    organizacao = models.CharField(max_length=30, null=True)
    inicio_curso = models.DateField(default=datetime.now, null=True)
    termino_curso= models.DateField(default=datetime.now, null=True)
    horas = models.CharField(max_length=30, null=True)


# Habilidades
class Habilidades(models.Model):
    habilidades = models.CharField(max_length=30, null=True)

# Hobbies
class Hobbies(models.Model):
    hobbies = models.CharField(max_length=30, null=True)


    





