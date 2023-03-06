from rest_framework.serializers import ModelSerializer

from apps.models import Category, SubCategory, Shop, Product, Cart, Report, Order, Favourite, ProductImage


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


class CartModelSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ReportModelSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class FavouriteModelSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'


class OrderModelSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
