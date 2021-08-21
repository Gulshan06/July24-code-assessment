from rest_framework import serializers
from librarian.models import Librarian

class LibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = ("enroll_code", "name", "address", "mobilenumber", "username", "password" )
