from django.contrib import admin
from .models import Category, Product, Reason, Provider, Company, Location, Stock, Movement, ShoppingList


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "description", ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['company', 'name', 'address', 'type']
    prepopulated_fields = {'slug': ('name',)}
    # inlines = [CompanyInline]


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["name", "favorite", "description", ]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ["company", "location", "product", "quantity", "user", "slug", ]
    company_pk = "company"
    location_pk = "location"
    # company_name = Company.objects.get(pk=int(company_pk))
    # location_name = Location.objects.get(pk=3)
    prepopulated_fields = {"slug": ("location",)}


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


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    # prepopulated_fields = {'slug': ('name',)}
    # inlines = [ProductInline]


@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'location_src', 'provider_src']
    # prepopulated_fields = {'slug': ('name',)}
    # inlines = [ProductInline]
