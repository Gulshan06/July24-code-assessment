from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctorcode=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    special=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)

   