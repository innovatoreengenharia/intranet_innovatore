# Generated by Django 4.2.3 on 2023-09-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "usuario",
            "0006_alter_cursos_inicio_curso_alter_cursos_termino_curso_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="cursos",
            name="descricao_curso",
            field=models.TextField(blank=True, null=True),
        ),
    ]