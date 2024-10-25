from django.conf import settings
from nav.models import Menu
from apps.catalogue.models import Category


def business(request):
    return {
        "razon_social": settings.BUSINESS_RAZON_SOCIAL,
        "calle": settings.BUSINESS_CALLE,
        "colonia": settings.BUSINESS_COLONIA,   
        "municipio": settings.BUSINESS_MUNICIPIO,
        "estado": settings.BUSINESS_ESTADO,
        "codigo_postal": settings.BUSINESS_CODIGO_POSTAL,
        "telefono": settings.BUSINESS_TELEFONO,
        "email": settings.BUSINESS_EMAIL,
        "logo": settings.BUSINESS_LOGO,
    }

def header(request):
    return {
        "menu": Menu.objects.all().order_by("order"),
    }
