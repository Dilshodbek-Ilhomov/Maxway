from django.contrib import admin
from .models import Category, Product, Order, OrderItem, PromoCode


# Mahsulot admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'emoji']
    prepopulated_fields = {'slug': ('name',)}  # slug avtomatik to'ldiriladi


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'is_hot']
    list_filter = ['category', 'is_available', 'is_hot']
    list_editable = ['price', 'is_available', 'is_hot']  # Ro'yxatda tahrirlash
    search_fields = ['name']


class OrderItemInline(admin.TabularInline):  # Buyurtma ichida elementlar
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'quantity', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'total_price', 'status', 'created_at']
    list_filter = ['status', 'payment', 'created_at']
    list_editable = ['status']  # Statusni ro'yxatda o'zgartirish
    readonly_fields = ['first_name', 'last_name', 'phone', 'address', 'total_price', 'created_at']
    inlines = [OrderItemInline]  # Buyurtma ichida mahsulotlarni ko'rish
    search_fields = ['first_name', 'last_name', 'phone']

@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount_percent', 'is_active', 'created_at']
    list_editable = ['is_active']


