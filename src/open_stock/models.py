from django.db import models
from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)


class Product(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    alarm_min_part = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)


class Reason(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    favorite = models.BooleanField(default=False)


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField()


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    type = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    slug = models.SlugField(unique=True)


class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location_src = models.ForeignKey(Location, on_delete=models.CASCADE)
    location_dest = models.ForeignKey(Location, on_delete=models.CASCADE)
    provider_src = models.ForeignKey(Provider, on_delete=models.CASCADE)


class ShoppingList(models.Model):
    provider_src = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    validate = models.BooleanField(default=False)
    location_dest = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
