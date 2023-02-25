from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField, SmallIntegerField, DecimalField, ForeignKey, \
    CASCADE, Model


class User(AbstractUser):
    pass


class Category(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(Model):
    title = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    category = ForeignKey(Category, on_delete=CASCADE, related_name='categories')
    owner = ForeignKey(User, CASCADE)

    def __str__(self):
        return f'{self.title}'


class SubCategory(Model):
    name = CharField(max_length=100)
    category = ForeignKey(Category, on_delete=CASCADE, related_name='subcategories')


class Favourite(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='products')
    user = ForeignKey(User, on_delete=CASCADE, related_name='users')

    def __str__(self):
        return f'{self.user.email}({self.user.id}) -> {self.product.title}'


class Cart(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='products')
    user = ForeignKey(User, on_delete=CASCADE, related_name='users')
    quantity = SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.id} - {self.product.title} ({self.quantity})'
