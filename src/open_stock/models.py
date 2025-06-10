from django.db import models
from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Catégorie'


class Location(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    type = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Localisation'


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',
                                 blank=True, null=True, verbose_name="Catégorie")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='locations',
                                 blank=True, null=True, verbose_name="Rangement")
    count_mini_alarm = models.IntegerField(default=0, verbose_name="Alarme stock mini")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                default=0, null=True, verbose_name="Prix")
    sku = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produit'


class Reason(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Raison'


class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    favorite = models.BooleanField(default=False)
    # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fournisseur'


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True)


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Stockage'


class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location_src = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="source")
    location_dest = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="destination")
    provider_src = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="provider")

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Mouvement'


class ShoppingList(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    provider_src = models.ForeignKey(Provider, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True)
    validate = models.BooleanField(default=False)
    location_dest = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.created_date} par {self.user}"

    class Meta:
        verbose_name = 'Liste de course'
