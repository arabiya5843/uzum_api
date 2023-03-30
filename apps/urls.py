from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import CategoryModelViewSet, ShopModelViewSet, ProductModelViewSet, CartModelViewSet, \
    WishlistModelViewSet, OrderModelViewSet, FavouriteModelViewSet, SubCategoryModelViewSet, ProductImageModelViewSet

from apps.user.views import ClientModelViewSet, MerchantModelViewSet, UserViewSet


router = DefaultRouter()
router.register('category', CategoryModelViewSet, 'category')
router.register('subcategory', SubCategoryModelViewSet, 'subcategory')
router.register('shop', ShopModelViewSet, 'shop')
router.register('product', ProductModelViewSet, 'product')
router.register('product-image', ProductImageModelViewSet, 'product_image')
router.register('cart', CartModelViewSet, 'cart')
router.register('favourite', FavouriteModelViewSet, 'favourite')
router.register('wishlist', WishlistModelViewSet, 'report')
router.register('order', OrderModelViewSet, 'order')
router.register('user', UserViewSet, 'user')
router.register('client', ClientModelViewSet, 'client')
router.register('merchant', MerchantModelViewSet, 'merchant')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('apps.user.urls')),

]
