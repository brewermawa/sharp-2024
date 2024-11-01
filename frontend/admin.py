from django.contrib import admin
from oscar.core.loading import get_model

Slider = get_model("frontend", "Slider")

@admin.register(Slider)
class MenuAdmin(admin.ModelAdmin):
    pass
