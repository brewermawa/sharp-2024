from oscar.apps.catalogue.views import CatalogueView as BaseCatalogueView


class CatalogueView(BaseCatalogueView):
    template_name = "oscar/catalogue/index.html"
    
    