from django.shortcuts import render
from django.views import generic
from oscar.core.loading import get_class, get_model

Slider = get_model("frontend", "Slider")


class DashboardSliderListView(generic.ListView):
    model = Slider
    template_name = "dashboard/frontend/slider_list.html"
    context_object_name = "slider_list"
