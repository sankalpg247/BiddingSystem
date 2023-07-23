from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    weight = models.FloatField()
    deliveryCharges = models.FloatField()
    expiryDate = models.DateField()
    imgPath = models.CharField(max_length=1000, default='')
