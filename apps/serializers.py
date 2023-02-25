from rest_framework.serializers import ModelSerializer

from apps.models import Category, Product, Cart, Favourite, SubCategory


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')



class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'parent')



class CartModelSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"



class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"



class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"







