from django.shortcuts import render
from django.views import generic
from oscar.core.loading import get_class, get_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.template.loader import render_to_string

Slider = get_model("frontend", "Slider")
SliderCreateUpdateForm = get_class("frontend.dashboard.forms", "DashboardSliderCreateUpdateForm")


class DashboardSliderListView(generic.ListView):
    model = Slider
    template_name = "dashboard/frontend/slider_list.html"
    context_object_name = "slider_list"


class DashboardSliderCreateView(generic.CreateView):
    model = Slider
    template_name = "dashboard/frontend/menu_update.html"
    form_class = SliderCreateUpdateForm
    success_url = reverse_lazy("frontend-dashboard:slider-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = "Create new slider"
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
            "dashboard/frontend/messages/slider_saved.html", {"frontend": self.object}
        )
        messages.success(self.request, msg, extra_tags="safe")

        return response



class DashboardSliderUpdateView(generic.UpdateView):
    model = Slider
    template_name = "dashboard/frontend/slider_update.html"
    form_class = SliderCreateUpdateForm
    success_url = reverse_lazy("frontend-dashboard:slider-list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["title"] = f"Editando slider: {self.object.name}"
        return ctx

    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors",
        )
        return super().forms_invalid(form, inlines)

    def forms_valid(self, form, inlines):
        msg = render_to_string(
            "dashboard/frontend/messages/slider_saved.html", {"frontend": self.object}
        )
        messages.success(self.request, msg, extrforms_valida_tags="safe")
        return super().forms_valid(form, inlines)



class DashboardSliderDeleteView(generic.DeleteView):
    model = Slider
    template_name = "dashboard/frontend/slider_delete.html"
    success_url = reverse_lazy("frontend-dashboard:slider-list")