# Generated by Django 4.2.3 on 2023-08-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gestao", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qualidade",
            name="doc",
            field=models.FileField(blank=True, upload_to="docs/qualidade/%Y/%m/"),
        ),
    ]