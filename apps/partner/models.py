from django.db import models

from oscar.apps.partner.abstract_models import AbstractStockRecord

class StockRecord(AbstractStockRecord):
    discounted_price = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)

from oscar.apps.partner.models import * 
 