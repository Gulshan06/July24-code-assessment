from rest_framework import serializers
from book.models import Books


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ("bookname", "author", "description", "publisher", "price" )
