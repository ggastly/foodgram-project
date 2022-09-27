import base64

from django.core.files.base import ContentFile
from rest_framework import serializers
import webcolors


from recipes.models import Tag, Ingridient, Recipe


class Hex2NameColor(serializers.Field):
    def to_representation(self, value):
        return value
    def to_internal_value(self, data):
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class RecipeSerializer(serializers.ModelSerializer):
    
    image = Base64ImageField(required=True, allow_null=False)
    
    class Meta:
        model = Recipe
        fields = (
            'ingridients',
            'tags',
            'image',
            'name',
            'text',
            'cooking_time'
            )


class RecipeReadOnlySerializer(serializers.ModelSerializer):

    image = Base64ImageField(required=True, allow_null=False)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'tags',
            'author',
            'ingridients',
            'is_favorited',
            'is_in_shopping_cart',
            'image',
            'name',
            'text',
            'cooking_time'
        )


class ShoppingCartSerializer(serializers.ModelSerializer):
    image = Base64ImageField(read_only=True)
    
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'image',
            'cooking_time'
        )
        read_only_fields = (
            'id',
            'name',
            'image',
            'cooking_time'
        )


class TagSerializer(serializers.ModelSerializer):

    color = Hex2NameColor()

    class Meta:
        model = Tag
        fields = ('id', 'color', 'name', 'slug')


class IngridientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingridient
        fields = ('id', 'name', 'measurement_unit')