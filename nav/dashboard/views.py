from django.contrib import messages
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views import generic
from oscar.core.loading import get_class, get_model

Menu = get_model("nav", "Menu")
MenuCreateUpdateForm = get_class("nav.dashboard.forms", "DashboardMenuCreateUpdateForm")


class DashboardMenuListView(generic.ListView):
    model = Menu
    template_name = "dashboard/nav/menu_list.html"
    context_object_name = "menu_list"


class DashboardMenuCreateView(generic.CreateView):
    model = Menu
    template_name = "dashboard/nav/menu_update.html"
    form_class = MenuCreateUpdateForm
    success_url = reverse_lazy("nav-dashboard:menu-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "Create new menu option"
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors",
        )
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        response = super().forms_valid(form, inlines)

        msg = render_to_string(
            "dashboard/nav/messages/menu_saved.html", {"nav": self.object}
        )
        messages.success(self.request, msg, extra_tags="safe")

        return response


class DashboardMenuUpdateView(generic.UpdateView):
    model = Menu
    template_name = "dashboard/nav/menu_update.html"
    form_class = MenuCreateUpdateForm
    success_url = reverse_lazy("nav-dashboard:menu-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = self.object.name
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors",
        )
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        msg = render_to_string(
            "dashboard/nav/messages/boutique_saved.html", {"nav": self.object}
        )
        messages.success(self.request, msg, extrforms_valida_tags="safe")
        return super().forms_valid(form, inlines)


class DashboardMenuDeleteView(generic.DeleteView):
    model = Menu
    template_name = "dashboard/nav/menu_delete.html"
    success_url = reverse_lazy("nav-dashboard:menu-list")
