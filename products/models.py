from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=15, validators=[MinLengthValidator(10)])

    image = models.ImageField(
        null=True, blank=True, upload_to='media/fotos')
    description = models.TextField()

    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f'{self.sku} | {self.name} - ${self.price}'
