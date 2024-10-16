from django.db import models

from apps.catalogue.models import Category, Product


class Menu(models.Model):
    name = models.CharField(max_length=25, unique=True, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    url = models.CharField(null=True, blank=True)
    order = models.SmallIntegerField()
