from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views import generic
from oscar.core.loading import get_class, get_model

Menu = get_model("nav", "Menu")
MenuCreateUpdateForm = get_class("nav.dashboard.forms", "DashboardBoutiqueCreateUpdateForm")


class DashboardMenuListView(generic.ListView):
    model = Menu
    template_name = "dashboard/nav/men_list.html"
    context_object_name = "menu_list"