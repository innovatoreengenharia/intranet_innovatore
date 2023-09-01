# Generated by Django 4.2 on 2023-08-31 20:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("usuario", "0004_alter_perfil_foto_alter_perfil_sobrenome_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cursos",
            name="perfil",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="usuario.perfil",
            ),
        ),
        migrations.AddField(
            model_name="formacao",
            name="perfil",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="usuario.perfil",
            ),
        ),
        migrations.AddField(
            model_name="habilidades",
            name="perfil",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="usuario.perfil",
            ),
        ),
        migrations.AddField(
            model_name="hobbies",
            name="perfil",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="usuario.perfil",
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="bairro",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="cargo",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="cargo_inicial",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="cidade_trabalho",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="data_inicio",
            field=models.DateField(
                blank=True, default=datetime.datetime.now, null=True
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="data_mudanca",
            field=models.DateField(
                blank=True, default=datetime.datetime.now, null=True
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="email_empresa",
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="endereco",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="estado",
            field=models.CharField(
                choices=[
                    ("Acre", "AC"),
                    ("Alagoas", "AL"),
                    ("Amapá", "AP"),
                    ("Amazonas", "AM"),
                    ("Bahia", "BA"),
                    ("Ceará", "CE"),
                    ("Distrito Federal", "DF"),
                    ("Espírito Santo", "ES"),
                    ("Goiás", "GO"),
                    ("Maranhão", "MA"),
                    ("Mato Grosso", "MT"),
                    ("Mato Grosso do Sul", "MS"),
                    ("Minas Gerais", "MG"),
                    ("Pará", "PA"),
                    ("Paraíba", "PB"),
                    ("Paraná", "PR"),
                    ("Pernambuco", "PE"),
                    ("Piauí", "PI"),
                    ("Rio de Janeiro", "RJ"),
                    ("Rio Grande do Norte", "RN"),
                    ("Rio Grande do Sul", "RS"),
                    ("Rondônia", "RO"),
                    ("Roraima", "RR"),
                    ("Santa Catarina", "SC"),
                    ("São Paulo", "SP"),
                    ("Sergipe", "SE"),
                    ("Tocantins", "TO"),
                ],
                default="AC",
                max_length=30,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="estado_trabalho",
            field=models.CharField(
                choices=[
                    ("Acre", "AC"),
                    ("Alagoas", "AL"),
                    ("Amapá", "AP"),
                    ("Amazonas", "AM"),
                    ("Bahia", "BA"),
                    ("Ceará", "CE"),
                    ("Distrito Federal", "DF"),
                    ("Espírito Santo", "ES"),
                    ("Goiás", "GO"),
                    ("Maranhão", "MA"),
                    ("Mato Grosso", "MT"),
                    ("Mato Grosso do Sul", "MS"),
                    ("Minas Gerais", "MG"),
                    ("Pará", "PA"),
                    ("Paraíba", "PB"),
                    ("Paraná", "PR"),
                    ("Pernambuco", "PE"),
                    ("Piauí", "PI"),
                    ("Rio de Janeiro", "RJ"),
                    ("Rio Grande do Norte", "RN"),
                    ("Rio Grande do Sul", "RS"),
                    ("Rondônia", "RO"),
                    ("Roraima", "RR"),
                    ("Santa Catarina", "SC"),
                    ("São Paulo", "SP"),
                    ("Sergipe", "SE"),
                    ("Tocantins", "TO"),
                ],
                default="AC",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="nascimento",
            field=models.DateField(
                blank=True, default=datetime.datetime.now, null=True
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="numero",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="obra_trabalho",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="rg",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="setor",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="sexo",
            field=models.CharField(
                choices=[("masculino", "M"), ("feminino", "F")],
                default="M",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="sobrenome",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="telefone",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="usuario",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
