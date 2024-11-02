from django.db import models
from oscar.apps.catalogue.models import Category, Product


class Slider(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    image = models.ImageField(upload_to="sliders/", blank=False, null=False)
    title = models.CharField(max_length=50, blank=False, null=False)
    message = models.CharField(max_length=50, blank=False, null=False)
    button_text = models.CharField(max_length=10, blank=False, null=False)
    url = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "frontend"
