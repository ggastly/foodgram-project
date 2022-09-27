from recipes.models import Ingridient, Recipe, Tag
from recipes.serializers import (IngridientSerializer,
                                 RecipeReadOnlySerializer, RecipeSerializer,
                                 ShoppingCartSerializer, TagSerializer)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return RecipeReadOnlySerializer
        elif self.request.path == '/api/recipes/1/shopping_cart/':
            return ShoppingCartSerializer
        else:
            return RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    @action(
        detail=True,
        methods=['post', 'delete'],
        serializer_class=ShoppingCartSerializer
    )
    def shopping_cart(self, request, pk):
        instance = Recipe.objects.get(id=pk)
        if request.method == 'DELETE':
            instance.is_in_shopping_cart = False
        else:
            instance.is_in_shopping_cart = True
        instance.save()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save
        return Response(serializer.data)


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngridientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingridient.objects.all()
    serializer_class = IngridientSerializer
