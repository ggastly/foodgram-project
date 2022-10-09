from django.contrib import admin

from recipes.models import (FavoriteRecipe, Ingredient, Recipe,
                            RecipeIngredient, ShoppingCart, Tag)


class BaseAdminSettings(admin.ModelAdmin):
    empty_value_display = '-пусто-'


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 0


@admin.register(Tag)
class TagAdmin(BaseAdminSettings):
    list_display = (
        'name',
        'color',
        'slug'
    )
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )


@admin.register(Ingredient)
class IngredientAdmin(BaseAdminSettings):
    list_display = (
        'name',
        'measurement_unit'
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('name', )


@admin.register(Recipe)
class RecipeAdmin(BaseAdminSettings):
    list_display = (
        'name',
        'author',
        'in_favorite'
    )
    list_display_links = ('name',)
    search_fields = ('name',)
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('in_favorite',)
    filter_horizontal = ('tags',)
    inlines = (RecipeIngredientInline,)
    ordering = ('-pub_date',)

    def in_favorite(self, obj):
        return obj.in_favorite.count()


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = (
        'recipe',
        'ingredient',
        'amount',
    )
    list_filter = ('recipe', 'ingredient')


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', )
    list_filter = ('user', )
    search_fields = ('user', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', )
    list_filter = ('user', )
    search_fields = ('user', )