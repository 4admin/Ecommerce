# Generated by Django 5.1 on 2024-08-20 17:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loja", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="imagem",
            field=models.ImageField(upload_to=""),
        ),
    ]
