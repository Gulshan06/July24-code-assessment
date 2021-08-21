from django.db import models

# Create your models here.

#(enroll_code, name, address, mobilenumber, username, password )

class Librarian(models.Model):
    enroll_code = models.IntegerField()
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    mobilenumber = models.BigIntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
