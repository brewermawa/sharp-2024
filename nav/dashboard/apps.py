from django.urls import path
from oscar.core.application import OscarDashboardConfig
from oscar.core.loading import get_class


class DashboardConfig(OscarDashboardConfig):
    name = "nav.dashboard"
    label = "nav_dashboard"
    namespace = "nav-dashboard"

    #default_permissions = ["is_staff"]

    def ready(self):
        self.menu_list_view = get_class("nav.dashboard.views", "DashboardMenuListView")

    def get_urls(self):
        urls = [
            path("", self.menu_list_view.as_view(), name="menu-list"),
        ]
        return self.post_process_urls(urls)

