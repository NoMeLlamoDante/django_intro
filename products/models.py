from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=15, validators=[MinLengthValidator(10)])
    description = models.TextField()

    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products", null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='media/fotos')

    price = models.DecimalField(max_digits=10, decimal_places=2)

    creation_date = models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.sku} | {self.name} - ${self.price}'


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Comments(models.Model):
    text = models.TextField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True,
        related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )
    creation_date = models.TimeField(default=timezone.now)

    def __str__(self):
        return self.text[:14] if len(self.text) > 15 else self.text
