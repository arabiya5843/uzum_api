from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import F, Sum

from apps.user.permissions import IsOwner
from apps.filters import ProductFilter
from apps.models import Product, Category, Shop, ProductImage, Favourite, Cart, Report, Order, SubCategory
from apps.serializers import ProductModelSerializer, CategoryModelSerializer, ProductImageModelSerializer, \
    ShopModelSerializer, CartModelSerializer, FavouriteModelSerializer, ReportModelSerializer, OrderModelSerializer, SubCategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['price']
    permission_classes = (IsAuthenticated, IsOwner,)

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageModelSerializer


class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    @action(['GET'], False, 'report', 'report')
    def get_carts_count(self, request):
        count = self.get_queryset().filter(status='accepted').aggregate(Sum('quantity'))
        return Response({'Sotilgan mahsulot: ': count.get('quantity__sum')})


class FavouriteModelViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteModelSerializer


class ReportModelViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportModelSerializer


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_queryset(self):
        qs = super().get_queryset()
        data = self.request.data
        cart = data.get('cart')
        product = data.get('product')
        quantity = Cart.objects.get(pk=cart).quantity
        Product.objects.filter(pk=product).update(amount=F('amount') - quantity)
        Cart.objects.filter(pk=cart).update(status='accepted')
        return qs



