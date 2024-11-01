from django import forms
from oscar.core.loading import get_model

Slider = get_model("frontend", "Slider")

class DashboardSliderCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ("name", "image", "title", "message", "button_text" "url", "category", "product", )
