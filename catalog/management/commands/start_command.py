from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Информация для отношения Category
        category_list = [
            {'pk': 1, 'name': 'Игрушки для мальчиков',
             'description': 'Включает в себя машины, автоматы, роботов и др.'},
            {'pk': 2, 'name': 'Игрушки для девочек',
             'description': 'Включает в себя кукл, дома и мебель для кукол, детская косметика и др.'},
            {'pk': 3, 'name': 'Настольные игры', 'description': 'Включает в себя настольные и уличные игры'}
        ]
        # Вносим данные в БД
        category_for_create = []
        for list_item in category_list:
            category_for_create.append(
                Category(**list_item)
            )
        Category.objects.bulk_create(category_for_create)
        # Информация для отношения Product
        product_list = [
            {'pk': 1, 'name': 'Автомат',
             'description': 'Автомат имеет световые и звуковые эффекты. Работает от трех элементов питания типа АА',
             'category_product': Category.objects.get(pk=1), 'price': 200.00},
            {'pk': 2, 'name': 'Машина на р/у',
             'description': 'Игрушка подходит для игры на улице в сухую погоду. Работает от аккумулятора (зарядное уст-во в комплекте)',
             'category_product': Category.objects.get(pk=1), 'price': 150.00},
            {'pk': 3, 'name': 'Кукла Barby Extra',
             'description': 'Размер куклы 30см. В комплекте элементы одежды, домашнее животное(1 шт)',
             'category_product': Category.objects.get(pk=2), 'price': 230.00},
            {'pk': 4, 'name': 'Дом для куклы',
             'description': 'Размер в собранном виде(В*Ш*Д): 900*250*600мм. В комплекте мебель для кухни',
             'category_product': Category.objects.get(pk=2), 'price': 600.00},
            {'pk': 5, 'name': 'Настольная игра Anno 1800',
             'description': 'Рекомендуемый возраст: 14+, Кол-во игроков: от 2 до 4, Примерное время игры ~120 мин',
             'category_product': Category.objects.get(pk=3), 'price': 500.00}
        ]
        # Вносим данные в БД
        product_for_create = []
        for list_item in product_list:
            product_for_create.append(
                Product(**list_item)
            )
        Product.objects.bulk_create(product_for_create)
