from oscar.apps.catalogue.views import CatalogueView as BaseCatalogueView
from oscar.core.loading import get_model

Slider = get_model("frontend", "Slider")
Promo = get_model("frontend", "Promo")
Range = get_model("offer", "Range")


class CatalogueView(BaseCatalogueView):
    template_name = "oscar/catalogue/index.html"
    
    def get_context_data(self, **kwargs):
        ctx = {}
        ctx["summary"] = "All products"
        ctx["sliders"] = Slider.objects.all()
        ctx["promos"] = Promo.objects.all()
        ctx["featured"] = Range.objects.get(name="featured").all_products()
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name
        )
        ctx.update(search_context)
        return ctx