from django.urls import path
from oscar.core.application import OscarDashboardConfig
from oscar.core.loading import get_class


class DashboardConfig(OscarDashboardConfig):
    name = "nav.dashboard"
    label = "nav_dashboard"
    namespace = "nav-dashboard"

    default_permissions = ["is_staff"]

    def ready(self):
        self.menu_list_view = get_class("nav.dashboard.views", "DashboardMenuListView")
        self.menu_create_view = get_class("nav.dashboard.views", "DashboardMenuCreateView")
        self.menu_update_view = get_class("nav.dashboard.views", "DashboardMenuUpdateView")
        self.menu_delete_view = get_class("nav.dashboard.views", "DashboardMenuDeleteView")


    def get_urls(self):
        urls = [
            path("", self.menu_list_view.as_view(), name="menu-list"),
            path("create/", self.menu_create_view.as_view(), name="menu-create"),
            path("update/<int:pk>", self.menu_update_view.as_view(), name="menu-update"),
            path("delete/<int:pk>", self.menu_delete_view.as_view(), name="menu-delete"),
        ]
        return self.post_process_urls(urls)

