from django import forms

from catalog.models import Product, Category, Version, BlogPost

danger_words = (
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дёшево',
    'бесплатно',
    'обман',
    'полиция',
    'радар',
)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category_product', 'price', 'status_of_product',)

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        for field_name, field in self.fields.items():
#            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        for word in danger_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Название содержит некорректное слово: {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        for word in danger_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Описание содержит некорректное слово: {word}')

        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'preview', 'is_published',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
