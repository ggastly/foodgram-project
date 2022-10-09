# Generated by Django 4.1.1 on 2022-10-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="measurement_unit",
            field=models.CharField(max_length=15, verbose_name="Единицы измерения"),
        ),
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(
                max_length=70, unique=True, verbose_name="Название ингридиента"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=models.CharField(
                max_length=20, unique=True, verbose_name="Цвет тега"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(
                max_length=50, unique=True, verbose_name="Название тега"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(max_length=100, unique=True, verbose_name="Slug"),
        ),
    ]
