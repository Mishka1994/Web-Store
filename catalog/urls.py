from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, CatalogListView, BlogPostCreateView, BlogPostDetailView, BlogPostListView, \
    BlogPostUpdateView, BlogPostDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('catalog/page_with_products/', CatalogListView.as_view(), name='page_with_products'),
    path('catalog/contacts/', contacts, name='contacts'),
    path('create/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view_blogpost'),
    path('list/', BlogPostListView.as_view(), name='list_blogpost'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='update_blogpost'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blogpost')

]
