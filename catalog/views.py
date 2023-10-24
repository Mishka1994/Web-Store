from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, CategoryForm, VersionForm, BlogPostForm, ProductFormManagers
from catalog.models import Product, BlogPost, Category, Version


def base(request):
    return render(request, 'base.html')


class IndexTemplateView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'
        return context


def index(request):
    context = {
        'title': 'Main'
    }
    return render(request, 'catalog/index.html', context)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:list_product')


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:list_product')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'

    success_url = reverse_lazy('catalog:list_product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid:
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

#    def test_func(self):
#        return self.request.user.is_staff

#    def get_form_class(self):
#        if self.object.creator == self.request.user:
#            return ProductForm
#        elif self.test_func():
#            return ProductFormManagers
#        else:
#            return ProductForm


class ProductManagersUpdate(UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductFormManagers
    success_url = reverse_lazy('catalog:list_product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid:
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


    def test_func(self):
        return self.request.user.is_staff


class ProductListView(PermissionRequiredMixin, ListView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.view_product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            last_version = product.version_set.filter(current_version_indicator=True).first()
            if last_version:
                product.last_version_number = last_version.version_number
                product.last_version_name = last_version.name_version
            else:
                product.last_version_number = None
                product.last_version_name = None

        return context_data


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:list_product')


class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contacts.html'


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('catalog:list_blogpost')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)


class BlogPostDetailView(LoginRequiredMixin, DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogPostListView(LoginRequiredMixin, ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_blogpost', args=[self.kwargs.get('pk')])


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('catalog:list_blogpost')


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:list_version')


class VersionListView(LoginRequiredMixin, ListView):
    model = Version


class VersionDetailView(LoginRequiredMixin, DetailView):
    model = Version


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
