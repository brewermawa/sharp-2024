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


    def get_urls(self):
        urls = [
            path("", self.slider_list_view.as_view(), name="slider-list"),
        ]

        return self.post_process_urls(urls)
        
