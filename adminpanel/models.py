from django.db import models


class MainPageInfo(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
    description = models.TextField('Краткий текст', null=True, blank=True)
    image = models.ImageField(upload_to='', null=True, blank=True)

