# Generated by Django 4.2.3 on 2023-08-25 20:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("usuario", "0003_delete_sobre_perfil_texto_experiencia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfil",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos"),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="sobrenome",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="perfil",
            name="usuario",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
