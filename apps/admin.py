from django.contrib import admin
from apps.models import Category, Shop, Product, Cart, Wishlist, Order, Favourite, SubCategory

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Favourite)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
