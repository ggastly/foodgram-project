# Generated by Django 4.1.1 on 2022-10-08 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0010_alter_shoppingcart_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ingredient",
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
            },
        ),
    ]
