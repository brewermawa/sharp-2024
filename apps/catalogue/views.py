from oscar.apps.catalogue.views import CatalogueView as BaseCatalogueView
from oscar.core.loading import get_model

Slider = get_model("frontend", "Slider")


class CatalogueView(BaseCatalogueView):
    template_name = "oscar/catalogue/index.html"
    
    def get_context_data(self, **kwargs):
        ctx = {}
        ctx["summary"] = "All products"
        ctx["sliders"] = Slider.objects.all()
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name
        )
        ctx.update(search_context)
        return ctx