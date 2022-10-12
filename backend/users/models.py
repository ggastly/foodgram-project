from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(
        verbose_name='Email',
        help_text='Адрес электронной почты',
        unique=True
    )

    id = models.BigAutoField(primary_key=True)

    username = models.CharField(
        verbose_name='Никнейм',
        help_text='Никнейм',
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        verbose_name='Имя',
        help_text='Имя пользователя',
        max_length=20,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        help_text='Фамилия пользователя',
        max_length=30,
    )
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    class Meta:
        ordering = ('id', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Подписанный пользователь'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор',
        help_text='Автор, на которого можно подписаться'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='user_is_author',
            ),
        )

    def __str__(self):
        return f'{self.user.username} подписан на {self.author.username}'
