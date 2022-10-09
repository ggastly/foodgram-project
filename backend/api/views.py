from django.db.models import F, Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.filters import IngredientSearchFilter, RecipeFilterSet
from api.pagination import CustomPagination
from api.permissions import IsAuthenticatedOwnerOrReadOnly
from api.serializers import (FavoriteRecipeSerializer, IngredientSerializer,
                             RecipeListSerializer, RecipeSerializer,
                             ShoppingCartSerializer, SubscribeListSerializer,
                             SubscribeSerializer, TagSerializer)
from recipes.models import (FavoriteRecipe, Ingredient, Recipe,
                            RecipeIngredient, ShoppingCart, Tag)
from users.models import Subscribe, User


class UsersViewSet(UserViewSet):
    pagination_class = CustomPagination

    @action(
        methods=['GET'],
        detail=False
    )
    def subscriptions(self, request):
        subscriptions_list = self.paginate_queryset(
            User.objects.filter(following__user=request.user)
        )
        serializer = SubscribeListSerializer(
            subscriptions_list, many=True, context={
                'request': request
            }
        )
        return self.get_paginated_response(serializer.data)

    @action(
        methods=['POST', 'DELETE'],
        detail=True
    )
    def subscribe(self, request, id):
        if request.method != 'POST':
            subscription = get_object_or_404(
                Subscribe,
                author=get_object_or_404(User, id=id),
                user=request.user
            )
            self.perform_destroy(subscription)
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = SubscribeSerializer(
            data={
                'user': request.user.id,
                'author': get_object_or_404(User, id=id).id
            },
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecipeFilterSet
    permission_classes = (IsAuthenticatedOwnerOrReadOnly, )

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return RecipeListSerializer
        elif self.action == 'shopping_cart':
            return ShoppingCartSerializer
        elif self.action == 'favorite':
            return FavoriteRecipeSerializer
        return RecipeSerializer

    def method_for_actions(self, request, pk, model, serializer):
        if request.method == 'POST':
            serializer = serializer(
                data={'user': request.user.id, 'recipe': pk},
                context={'request': request}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        recipe = model.objects.filter(user=request.user, recipe__id=pk)
        recipe.delete()
        return Response({'detail': 'Рецепт удалён'},
                        status=status.HTTP_204_NO_CONTENT)

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=(IsAuthenticated, )
    )
    def favorite(self, request, pk):
        serializer = self.get_serializer_class()
        return self.method_for_actions(
            request=request,
            pk=pk,
            model=FavoriteRecipe,
            serializer=serializer
        )

    @action(
        methods=['POST', 'DELETE'],
        detail=True,
        permission_classes=(IsAuthenticated, )
    )
    def shopping_cart(self, request, pk):
        serializer = self.get_serializer_class()
        return self.method_for_actions(
            request=request,
            pk=pk,
            model=ShoppingCart,
            serializer=serializer
        )

    @action(
        detail=False,
        methods=['GET'],
        permission_classes=(IsAuthenticated,)
    )
    def download_shopping_cart(self, request):
        response = HttpResponse(content_type='text/plain')
        response['Content-Disposition'] = 'filename=shopping-cart.txt'
        shopping_list = RecipeIngredient.objects.filter(
            recipe__cart__user=request.user
        ).values(
            name=F('ingredient__name'),
            measurement_unit=F('ingredient__measurement_unit')
        ).annotate(amount=Sum('amount')).values_list(
            'ingredient__name', 'amount', 'ingredient__measurement_unit'
        )
        result = []
        for ingredient in shopping_list:
            result.append(
                f'{ingredient[0]} ({ingredient[2]}) – {ingredient[1]}\n'
            )
        response.writelines(result)
        return response


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AllowAny,)
    filter_backends = (IngredientSearchFilter,)
    search_fields = ('^name',)
