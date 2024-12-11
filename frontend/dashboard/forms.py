from django import forms
from oscar.core.loading import get_model

Slider = get_model("frontend", "Slider")
Promo = get_model("frontend", "Promo")


class DashboardSliderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ("name", "image", "title", "message", "message2", "button_text", "url", "category", "product", )


class DashboardPromoCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Promo
        fields = ("name", "image", "title", "button_text", "url", "category", "product", )
