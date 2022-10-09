from django.contrib import admin

from users.models import Subscribe, User


class BaseAdminSettings(admin.ModelAdmin):
    empty_value_display = '-пусто-'
    list_filter = ('email', 'username')


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


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'author'
    )
    list_display_links = ('id', 'user')
    search_fields = ('user',)
