# Generated by Django 4.2.6 on 2023-11-16 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='confirmada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='compra',
            name='endereco_entrega',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='forma_pagamento',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]