from django.contrib import admin
from .models import Category, Product, Reason, Provider, Company, Location, Stock, Movement, ShoppingList


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "location", "count_mini_alarm", "description", ]
    prepopulated_fields = {"slug": ("name",)}
    # inlines = [CategoryInline]


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'type']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductInline]
