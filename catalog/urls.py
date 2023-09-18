from django.urls import path

from catalog.views import index, index_2

urlpatterns = [
    path('', index),
    path('contacts/', index_2)
]
