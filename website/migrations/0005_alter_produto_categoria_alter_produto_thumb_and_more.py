# Generated by Django 4.2.6 on 2023-11-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_categoria_alter_produto_thumb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('SUPERIOR', 'Parte Superior'), ('INFERIOR', 'Parte Inferior'), ('UNICA', 'Peça Única'), ('TER_PECA', 'Terceira Peça'), ('ACESSORIOS', 'Acessórios'), ('CALÇADO', 'Calçado'), ('OUTROS', 'Outros')], max_length=100),
        ),
        migrations.AlterField(
            model_name='produto',
            name='thumb',
            field=models.ImageField(upload_to='img_produto'),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
