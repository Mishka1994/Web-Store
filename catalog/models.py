from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='product_preview/', verbose_name='превью изображение', **NULLABLE)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='цена')
    date_of_creation = models.DateField(auto_now_add=True, null=True)
    last_modified_date = models.DateField(auto_now=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                                verbose_name='Создатель продукта')
    status_of_product = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return f'{self.name} {self.description}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

        permissions = [
            (
                'set_status_of_product',
                'Can status_of_product'
            ),
            (
                'set_description',
                'Can description'
            ),
            (
                'set_category_product',
                'Can category_product'
            )

        ]


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='url-метка', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog_post_preview/', verbose_name='превью поста', **NULLABLE)
    date_of_creation = models.DateField(auto_now_add=True, null=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='публикуется')
    number_of_views = models.IntegerField(default=0, verbose_name='счетчик просмотров')

    def __str__(self):
        return f'{self.title} ({self.is_published}, {self.date_of_creation})'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.CharField(max_length=50, verbose_name='версия продукта')
    name_version = models.CharField(max_length=100, verbose_name='название версии')
    current_version_indicator = models.BooleanField(default=True, verbose_name='индикатор текущей версии')

    def __str__(self):
        return f'{self.name_version} ({self.version_number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
