from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=200)
    pincode = models.IntegerField()
    plan=models.CharField(max_length=200)
    status=models.CharField(max_length=200)

    def __str__(self):
        return self.name

