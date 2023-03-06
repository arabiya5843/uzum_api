from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Shop, Product, Cart, Report, Order


@admin.register(Category)
class CategoryMPTTModelAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20


admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Report)
admin.site.register(Order)
