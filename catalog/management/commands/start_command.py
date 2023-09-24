from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()



        print('Сделано')
