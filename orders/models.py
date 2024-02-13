from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)


class Order(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=255)
    description = models.TextField(verbose_name="Описание", default="")
    category = models.ForeignKey(to=Category, verbose_name="Категория", on_delete=models.CASCADE)
