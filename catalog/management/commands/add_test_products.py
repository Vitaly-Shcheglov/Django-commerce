from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавляет тестовые продукты'

    def handle(self, *args, **options):
        Product.objects.all().delete()  # удаляем старые продукты
        # добавляем новые
        category = Category.objects.get(id=18)
        Product.objects.create(name="Новый продукт", description="Описание нового продукта", image="path/to/image.jpg", category=category, price=200.00)
