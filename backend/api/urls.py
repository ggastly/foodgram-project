from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import RecipeViewSet, TagViewSet, IngridientViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='Tag')
router.register(r'recipes', RecipeViewSet, basename='Recipe')
router.register(r'ingridients', IngridientViewSet, basename='Ingridient')


urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken'))
]