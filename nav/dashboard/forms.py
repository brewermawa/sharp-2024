from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model

Menu = get_model("nav", "Menu")


class DashboardBoutiqueCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("name", "url", "category", "product", "order")
