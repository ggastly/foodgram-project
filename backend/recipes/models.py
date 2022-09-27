from django.db import models
from users.models import User


class Ingridient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=25,
        blank=False,
        verbose_name='Название ингридиента',
        unique=True,
    )
    measurement_unit = models.CharField(
        max_length=20,
        verbose_name='Единицы измерения',
        blank=False,
    )


class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=25,
        blank=False,
        verbose_name='Название тега',
        unique=True,
    )
    color = models.CharField(
        max_length=16,
        blank=False,
        verbose_name='Цвет тега',
        unique=True,
    )
    slug = models.SlugField(
        max_length=70,
        verbose_name='Slug',
        unique=True,
    )



class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name='Теги',
        related_name='recipes'
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='recipes'
    )

    ingridients = models.ManyToManyField(
        Ingridient,
        blank=True,
        verbose_name='Ингридиенты',
        related_name='recipes'
    )

    is_favorited = models.BooleanField(default=False)
    is_in_shopping_cart = models.BooleanField(default=False)

    name = models.CharField(
        max_length=150,
        blank=False,
        verbose_name='Название рецепта',
    )
    image = models.ImageField(
        upload_to='recipes/images/', 
        blank=False,
        verbose_name='Финальный результат',
        )
    text = models.TextField(
        blank=False,
        verbose_name='Рецепт',
    )
    cooking_time = models.PositiveSmallIntegerField(
        blank=False,
        verbose_name='Время приготовления',
    )