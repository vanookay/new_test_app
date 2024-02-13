from django.contrib import admin

from orders.models import Order, Category


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
