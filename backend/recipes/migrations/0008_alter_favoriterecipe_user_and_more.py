# Generated by Django 4.1.1 on 2022-10-07 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipes", "0007_rename_recipes_favoriterecipe_recipe_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favoriterecipe",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorite_recipe",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="amount",
            field=models.PositiveSmallIntegerField(verbose_name="Количество"),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe_ingredient",
                to="recipes.ingredient",
                verbose_name="Ингредиент для рецепта",
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe_ingredient",
                to="recipes.recipe",
                verbose_name="Рецепт",
            ),
        ),
    ]
