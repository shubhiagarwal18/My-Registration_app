from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 256)
    phone = models.CharField(max_length = 10)
    dob = models.CharField(max_length =  256)

