from django.urls import path
from oscar.core.application import OscarDashboardConfig
from oscar.core.loading import get_class


class DashboardConfig(OscarDashboardConfig):
    name = 'frontend.dashboard'
    label = "frontend_dashboard"
    namespace = "frontend-dashboard"

    default_permissions = ["is_staff"]


    def ready(self):
        self.slider_list_view = get_class("frontend.dashboard.views", "DashboardSliderListView")
        self.slider_create_view = get_class("frontend.dashboard.views", "DashboardSliderCreateView")
        self.slider_update_view = get_class("frontend.dashboard.views", "DashboardSliderUpdateView")
        self.slider_delete_view = get_class("frontend.dashboard.views", "DashboardSliderDeleteView")


    def get_urls(self):
        urls = [
            path("", self.slider_list_view.as_view(), name="slider-list"),
            path("create/", self.slider_create_view.as_view(), name="slider-create"),
            path("update/<int:pk>", self.slider_update_view.as_view(), name="slider-update"),
            path("delete/<int:pk>", self.slider_delete_view.as_view(), name="slider-delete"),   
        ]

        return self.post_process_urls(urls)
        
