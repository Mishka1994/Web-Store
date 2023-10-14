from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import BlogPostCreateView, BlogPostDetailView, BlogPostListView, \
    BlogPostUpdateView, BlogPostDeleteView, ProductDetailView, ProductListView, ContactsTemplateView, IndexTemplateView, \
    ProductCreateView, ProductDeleteView, ProductUpdateView, CategoryCreateView, VersionCreateView, VersionListView, \
    VersionDetailView, VersionUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('list_product/', ProductListView.as_view(), name='list_product'),
    path('view_product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('edit_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('create/', BlogPostCreateView.as_view(), name='create_blogpost'),
    path('view_blogpost/<int:pk>/', BlogPostDetailView.as_view(), name='view_blogpost'),
    path('list_blogpost/', BlogPostListView.as_view(), name='list_blogpost'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='update_blogpost'),
    path('delete_blogpost/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blogpost'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('list_version/', VersionListView.as_view(), name='list_version'),
    path('view_version/<int:pk>/', VersionDetailView.as_view(), name='view_version'),
    path('edit_version/<int:pk>/', VersionUpdateView.as_view(), name='update_version')

]
