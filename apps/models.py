from django.db.models import CharField, TextField, DecimalField, ForeignKey, \
    CASCADE, Model, ImageField, IntegerField, DateTimeField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(Model):
    name = CharField(max_length=100)
    category = ForeignKey('Category', CASCADE)

    def __str__(self):
        return self.name


class Shop(BaseModel):
    name = CharField(max_length=50)
    description = TextField(max_length=512)
    image = ImageField(upload_to='shop_image/', null=True, blank=True)
    merchant = ForeignKey('user.User', CASCADE, related_name='merchant', null=True, blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=255)
    description = CharField(max_length=1000)
    image = ImageField(upload_to='images/', null=True, blank=True)
    price = DecimalField(max_digits=9, decimal_places=2)
    amount = IntegerField(default=1)
    category = ForeignKey(Category, CASCADE, related_name='product', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(Model):
    user = ForeignKey('user.User', CASCADE)
    product = ForeignKey('Product', CASCADE)
    quantity = IntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}"


class Favourite(Model):
    product = ForeignKey('Product', CASCADE)
    user = ForeignKey('user.User', CASCADE)

    def __str__(self):
        return f'{self.user.email}({self.user.id}) -> {self.product.name}'


class Cart(Model):
    product = ForeignKey('Product', CASCADE)
    user = ForeignKey('user.User', CASCADE)
    quantity = IntegerField(default=1)

    def __str__(self):
        return f'{self.product.name}'


class ProductImage(Model):
    image = ImageField(upload_to='shops/images/')
    product = ForeignKey('Product', CASCADE)


class Report(Model):
    product = ForeignKey('Product', CASCADE)
    user = ForeignKey('user.User', CASCADE)

    def __str__(self):
        return f'{self.product.name}'



