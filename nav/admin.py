from django.contrib import admin
from oscar.core.loading import get_model

Menu = get_model("nav", "Menu")

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass