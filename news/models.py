from django.db import models
from django.db.models.fields import CharField, DateField, TextField

class Public(models.Model):
    title = CharField('Заголовок', max_length=20)
    text = TextField('Статья', max_length=255)
    date = DateField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'      

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'     
