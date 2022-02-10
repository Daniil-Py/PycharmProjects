from django.db import models


class Info(models.Model):
    title = models.CharField('Название', max_length=100)
    info = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация'
        verbose_name_plural = 'Информации'

