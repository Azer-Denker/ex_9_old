from django.contrib.auth import get_user_model

from django.db import models


class Photo(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to='pics', verbose_name='Фотография')
    description = models.TextField(null=False, blank=False, max_length=2000, verbose_name='Подпись')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author_name = models.CharField(null=False, blank=False, max_length=50, verbose_name='Автор')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Comment(models.Model):
    photo = models.ForeignKey('webapp.Photo', related_name='comments', on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(max_length=400, verbose_name='Комментарий')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                               related_name='comments', verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
