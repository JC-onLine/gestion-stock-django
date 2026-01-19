from django.db import models
from account.models import CustomUser


class Company(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Compagnie'


class Location(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    type = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Localisation'


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Catégorie'


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produit'


class Provider(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    favorite = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fournisseur'


class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.product

    class Meta:
        verbose_name = 'Stockage'


class Reason(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Raison'


class Movement(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location_src = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="sources")
    location_dest = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="destinations")
    provider_src = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="providers")
    reason = models.ForeignKey(Reason, on_delete=models.CASCADE, related_name="reasons", null=True, blank=True)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.created_date} par {self.user}"

    class Meta:
        verbose_name = 'Liste de course'
