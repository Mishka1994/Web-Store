from django.db import models


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
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='product_preview/', verbose_name='превью изображение', **NULLABLE)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='цена')
    date_of_creation = models.DateField(auto_now_add=True, null=True)
    last_modified_date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.name} {self.category_product} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


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
