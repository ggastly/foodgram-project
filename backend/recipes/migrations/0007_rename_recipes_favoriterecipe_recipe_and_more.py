# Generated by Django 4.1.1 on 2022-10-07 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0006_alter_ingredient_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="favoriterecipe",
            old_name="recipes",
            new_name="recipe",
        ),
        migrations.RenameField(
            model_name="shoppingcart",
            old_name="recipes",
            new_name="recipe",
        ),
    ]