from django.db import models

# Create your models here.

class Order(models.Model):
    citizenName = models.CharField(max_length=200)
    productName = models.CharField(max_length=200)
    qty = models.IntegerField()
    amountPaid = models.FloatField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=200)