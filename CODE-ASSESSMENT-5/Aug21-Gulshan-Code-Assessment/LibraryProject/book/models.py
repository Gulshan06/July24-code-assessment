from django.db import models

# Create your models here.


#(bookname, author, description, publisher, price )


class Books(models.Model):
    bookname = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    publisher = models.CharField(max_length=200)
    price = models.IntegerField()