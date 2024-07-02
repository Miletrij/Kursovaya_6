from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name="заголовок")
    body = models.TextField(verbose_name="содержимое")
    image = models.ImageField(upload_to="Blogging/", verbose_name="Картинки", **NULLABLE)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    view_count = models.IntegerField(default=0, verbose_name='количество просмотров')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создан пользователем: ", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'многа блогафф'
