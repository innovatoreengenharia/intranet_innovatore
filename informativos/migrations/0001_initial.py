# Generated by Django 4.2.3 on 2023-12-11 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bloco",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagem",
                    models.ImageField(
                        blank=True, null=True, upload_to="informativos/imagem"
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("paragrafo", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Blocos",
            },
        ),
        migrations.CreateModel(
            name="Noticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "imagem",
                    models.ImageField(
                        blank=True, null=True, upload_to="informativos/imagem"
                    ),
                ),
                (
                    "imagem_destaque",
                    models.FileField(
                        blank=True, null=True, upload_to="informativos/imagem_destaque"
                    ),
                ),
                (
                    "imagem_thumb",
                    models.FileField(
                        blank=True, null=True, upload_to="informativos/imagem_thumb"
                    ),
                ),
                (
                    "imagem_noticia",
                    models.FileField(
                        blank=True, null=True, upload_to="informativos/imagem_noticia"
                    ),
                ),
                ("titulo", models.CharField(max_length=255)),
                ("paragrafo", models.TextField(blank=True, null=True)),
                ("destaque", models.BooleanField(default=False)),
                ("publicado_em", models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                "verbose_name_plural": "Notícias",
            },
        ),
    ]