from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Brand(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "brands"

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.code, self.name)


class Product(models.Model):
    sku = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.sku, self.name, self.price, self.brand)


class ProductActionLog(models.Model):
    # Constants in Model class
    ACTIONS = (
        ('create', 'creacion'),
        ('delete', 'eliminacion'),
        ('update', 'actualizacion'),
        ('read', 'lectura')
    )
    action = models.CharField(
        max_length=10,
        choices=ACTIONS,
        default='read'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "product_action_logs"


class Notification(models.Model):
    message = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    sent = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notifications"

