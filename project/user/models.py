from django.db import models

# Create your models here.
class Payment(models.Model):
    txnid = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    info = models.CharField(max_length=50)

class Order(models.Model):
    Orderid = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=50)
    pid = models.IntegerField()
    qty = models.IntegerField()
    pprice = models.CharField(max_length=10)
    amount=models.CharField(max_length=10)
    info = models.CharField(max_length=50)
