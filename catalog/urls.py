from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, page_with_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/page_with_products/', page_with_products, name='page_with_products'),
    path('catalog/contacts/', contacts, name='contacts'),

]
