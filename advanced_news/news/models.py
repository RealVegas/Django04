from django.db import models


# Create your models here.
class NewsPost(models.Model):
    n_title = models.CharField('Название новости', max_length=100)
    n_desc = models.CharField('Краткое описание новости', max_length=200)
    n_text = models.TextField('Новость')
    n_date = models.DateTimeField('Дата публикации')
    n_author = models.CharField('Автор', max_length=100)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.n_title