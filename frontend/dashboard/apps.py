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

        self.promo_list_view = get_class("frontend.dashboard.views", "DashboardPromoListView")
        self.promo_create_view = get_class("frontend.dashboard.views", "DashboardPromoCreateView")
        self.promo_update_view = get_class("frontend.dashboard.views", "DashboardPromoUpdateView")
        self.promo_delete_view = get_class("frontend.dashboard.views", "DashboardPromoDeleteView")


    def get_urls(self):
        urls = [
            path("slider/", self.slider_list_view.as_view(), name="slider-list"),
            path("slider/create/", self.slider_create_view.as_view(), name="slider-create"),
            path("slider/update/<int:pk>", self.slider_update_view.as_view(), name="slider-update"),
            path("slider/delete/<int:pk>", self.slider_delete_view.as_view(), name="slider-delete"),
            path("promo/", self.promo_list_view.as_view(), name="promo-list"),
            path("promo/create/", self.promo_create_view.as_view(), name="promo-create"),
            path("promo/update/<int:pk>", self.promo_update_view.as_view(), name="promo-update"),
            path("promo/delete/<int:pk>", self.promo_delete_view.as_view(), name="promo-delete"),
        ]

        return self.post_process_urls(urls)
        
