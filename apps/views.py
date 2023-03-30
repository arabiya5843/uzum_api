from contextlib import suppress
from datetime import timedelta, datetime

from django.db.models import F, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.filters import ProductFilter
from apps.models import Category, Shop, Product, Cart, Wishlist, Order, SubCategory, Favourite, ProductImage
from apps.serializers import CategoryModelSerializer, ShopModelSerializer, ProductModelSerializer, \
    WishlistModelSerializer, OrderCreateModelSerializer, CartModelSerializer
from apps.user.permissions import IsMerchant, IsMerchantOrReadOnly, IsClient, IsAdminUserOrReadOnly, IsAdminUser, \
    IsMerchantOrReadOnlyOrAdminUser


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]


class SubCategoryModelViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = [IsAdminUserOrReadOnly, IsAuthenticated]


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer
    permission_classes = [IsMerchantOrReadOnlyOrAdminUser, IsAuthenticated]


class ProductImageModelViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ShopModelSerializer
    permission_classes = [IsMerchantOrReadOnlyOrAdminUser,]


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = ProductFilter
    search_fields = ['name']
    ordering_fields = ['price']
    permission_classes = [IsAuthenticated, IsMerchantOrReadOnlyOrAdminUser]

    # def perform_create(self, serializer):
    #     # when a product is saved, its saved how it is the owner
    #     serializer.save(user=self.request.user)
    #
    # def get_queryset(self):
    #     # after get all products on DB it will be filtered by its owner and return the queryset
    #     merchant_queryset = self.queryset.filter(user=self.request.user)
    #     return merchant_queryset


class FavouriteModelViewSet(ModelViewSet):
    queryset = Favourite.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_queryset(self):
        user = self.request.user
        return Favourite.objects.filter(user=user)


class CartModelViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartModelSerializer
    permission_classes = [IsAuthenticated, IsClient]

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    @action(['GET'], False, 'report', 'report')
    def get_carts_count(self, request):
        count = self.get_queryset().filter(status='accepted').aggregate(Sum('quantity'))
        return Response({'Sotilgan mahsulot: ': count.get('quantity__sum')})
    # @action(['GET'], False, 'report', 'report')
    # def get_carts_count(self, request):
    #     last_month = datetime.today() - timedelta(days=30)
    #     qs = self.get_queryset()
    #     count = qs.filter(created_at__gte=last_month, status='accepted').aggregate(Sum('quantity'))
    #     shop = Shop.name
    #     return Response(
    #         {
    #             'shop': shop,
    #             'test': count.get('quantity__sum')
    #         }
    #     )


class WishlistModelViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistModelSerializer
    permission_classes = [IsAuthenticated, IsMerchant,]


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderCreateModelSerializer
    permission_classes = [IsAuthenticated, IsClient,]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)


