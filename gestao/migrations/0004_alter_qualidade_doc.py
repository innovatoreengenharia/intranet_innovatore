# Generated by Django 4.2.3 on 2023-08-24 13:58

from django.db import migrations, models
import gestao.models


class Migration(migrations.Migration):

    dependencies = [
        ("gestao", "0003_alter_qualidade_options_qualidade_subpasta_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qualidade",
            name="doc",
            field=models.FileField(
                blank=True, upload_to=gestao.models.Qualidade.get_doc_subpasta
            ),
        ),
    ]
