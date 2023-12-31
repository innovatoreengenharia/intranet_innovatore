# Generated by Django 4.2.3 on 2023-10-26 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0017_alter_perfil_estado_alter_perfil_estado_trabalho_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='post/')),
                ('texto_postagem', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.perfil')),
            ],
        ),
    ]
