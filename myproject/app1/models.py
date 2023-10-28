from django.db import models


# Create your models here.


class RegStore(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()


class ContactDetails(models.Model):
    name = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    service = models.CharField(max_length=100)
