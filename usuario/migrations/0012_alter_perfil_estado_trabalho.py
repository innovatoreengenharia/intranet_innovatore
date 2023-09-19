# Generated by Django 4.2.3 on 2023-09-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0011_alter_experiencia_empresa_alter_perfil_cpf_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfil",
            name="estado_trabalho",
            field=models.CharField(
                blank=True,
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
    ]
