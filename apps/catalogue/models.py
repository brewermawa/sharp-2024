from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    short_description = models.TextField(max_length=255, blank=True)

    def calculate_non_rating(self):
        return 5 - self.calculate_rating()

from oscar.apps.catalogue.models import * 
 