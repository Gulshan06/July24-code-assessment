from rest_framework import serializers
from patients.models import Hospital

class hospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields=('id','patient_code','name','address','email','phone','pincode','username','password')