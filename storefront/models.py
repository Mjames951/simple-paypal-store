from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(null=True)
    posted_at = models.DateTimeField(default=timezone.now)
    sold = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
