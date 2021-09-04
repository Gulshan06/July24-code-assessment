from django.db import models

# Create your models here.
class Hospital(models.Model):
    patient_code=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)
