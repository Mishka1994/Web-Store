from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import BlogPostCreateView, BlogPostDetailView, BlogPostListView, \
    BlogPostUpdateView, BlogPostDeleteView, ProductDetailView, ProductListView, ContactsTemplateView, IndexTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('list_product/', ProductListView.as_view(), name='list_products'),
    path('view_product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('create/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('view_blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='view_blogpost'),
    path('list_blogpost/', BlogPostListView.as_view(), name='list_blogpost'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='update_blogpost'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blogpost')

]
