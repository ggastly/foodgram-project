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
    list_filter = ('name', 'measurement_unit')


@admin.register(Recipe)
class RecipeAdmin(BaseAdminSettings):
    list_display = (
        'name',
        'author',
        'in_favorite'
    )
    list_display_links = ('name',)
    search_fields = ('name', 'author')
    list_filter = ('tags', )
    readonly_fields = ('in_favorite',)
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
    list_filter = (
        'recipe',
        'ingredient',
        'ingredient__measurement_unit',
    )
    search_fields = ('recipe', '^user__username', '^user__email')


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('recipe__tags', )
    search_fields = ('user__username', 'user__email', 'recipe')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    list_filter = ('recipe__tags', )
    search_fields = ('recipe', 'user__username', 'user__email')
