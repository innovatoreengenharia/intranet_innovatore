# Generated by Django 4.2.3 on 2023-09-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0004_alter_comercial_doc_alter_controladoria_doc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comercial',
            name='doc',
            field=models.FileField(upload_to='comercial/'),
        ),
        migrations.AlterField(
            model_name='controladoria',
            name='doc',
            field=models.FileField(upload_to='controladoria/'),
        ),
        migrations.AlterField(
            model_name='departamentopessoal',
            name='doc',
            field=models.FileField(upload_to='departamento_pessoal/'),
        ),
        migrations.AlterField(
            model_name='engenharia',
            name='doc',
            field=models.FileField(upload_to='engenharia/'),
        ),
        migrations.AlterField(
            model_name='financeiro',
            name='doc',
            field=models.FileField(upload_to='financeiro/'),
        ),
        migrations.AlterField(
            model_name='fiscal',
            name='doc',
            field=models.FileField(upload_to='fiscal/'),
        ),
        migrations.AlterField(
            model_name='juridico',
            name='doc',
            field=models.FileField(upload_to='juridico/'),
        ),
        migrations.AlterField(
            model_name='logistica',
            name='doc',
            field=models.FileField(upload_to='logistica/'),
        ),
        migrations.AlterField(
            model_name='marketing',
            name='doc',
            field=models.FileField(upload_to='marketing/'),
        ),
        migrations.AlterField(
            model_name='meioambiente',
            name='doc',
            field=models.FileField(upload_to='meio_ambiente/'),
        ),
        migrations.AlterField(
            model_name='orcamentos',
            name='doc',
            field=models.FileField(upload_to='orcamentos/'),
        ),
        migrations.AlterField(
            model_name='pmo',
            name='doc',
            field=models.FileField(upload_to='pmo/'),
        ),
        migrations.AlterField(
            model_name='qualidade',
            name='doc',
            field=models.FileField(upload_to='qualidade/'),
        ),
        migrations.AlterField(
            model_name='recursoshumanos',
            name='doc',
            field=models.FileField(upload_to='rh/'),
        ),
        migrations.AlterField(
            model_name='segurancadotrabalho',
            name='doc',
            field=models.FileField(upload_to='seguranca_trabalho/'),
        ),
        migrations.AlterField(
            model_name='sistemas',
            name='doc',
            field=models.FileField(upload_to='sistemas/'),
        ),
        migrations.AlterField(
            model_name='suprimentos',
            name='doc',
            field=models.FileField(upload_to='suprimentos/'),
        ),
        migrations.AlterField(
            model_name='ti',
            name='doc',
            field=models.FileField(upload_to='ti/'),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='doc',
            field=models.FileField(upload_to='vendas/'),
        ),
    ]
