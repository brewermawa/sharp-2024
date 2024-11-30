from django.db import models
from oscar.apps.catalogue.models import Category
from apps.catalogue.models import Product

class Menu(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'nav'