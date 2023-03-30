from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from apps.models import Category, SubCategory, Shop, Product, Cart, Wishlist, Order, Favourite, ProductImage


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ShopModelSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class CartModelSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class WishlistModelSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'


class OrderCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'product', 'cart', 'user')
        # fields = '__all__'


class CartReportModelSerializer(ModelSerializer):
    count = SerializerMethodField()


    class Meta:
        model = Cart
        fields = ()


class FavouriteModelSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
