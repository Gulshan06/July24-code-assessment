from django.db import models

class Studentapp(models.Model):
    name = models.CharField(max_length=20)
    address = models.IntegerField()
    clas = models.IntegerField()
    mob_num=models.CharField(max_length=50)
    username=models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    
    