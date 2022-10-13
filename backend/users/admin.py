from django.contrib import admin

from users.models import Subscribe, User


class BaseAdminSettings(admin.ModelAdmin):
    empty_value_display = '-пусто-'


@admin.register(User)
class UsersAdmin(BaseAdminSettings):
    list_display = (
        'id',
        'username',
        'email',
        'first_name',
        'last_name'
    )
    list_display_links = ('id', 'username')
    search_fields = ('username', )
    list_filter = ('is_superuser', 'is_staff')


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author'
    )
    list_display_links = ('id', 'user', 'author')
    search_fields = (
        'user__username',
        'user__email'
    )
