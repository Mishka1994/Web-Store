from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Product, BlogPost


def base(request):
    return render(request, 'base.html')


def index(request):
    context = {
        'title': 'Main'
    }
    return render(request, 'catalog/index.html', context)


class CatalogListView(ListView):
    model = Product
    template_name = 'catalog/page_with_products/page_with_products.html'


def contacts(request):
    context = {
        'title': 'Contacts'
    }
    return render(request, 'catalog/contacts/contacts.html', context)


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content', 'is_published')
    success_url = reverse_lazy('catalog:list_blogpost')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'is_published')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_blogpost', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:list_blogpost')
