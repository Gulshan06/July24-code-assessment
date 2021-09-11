from django.db import models
from django.db.models import fields
from rest_framework import serializers
from student.models import Studentapp

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Studentapp
        fields=( "name", "address", "clas", "mob_num", "username", "password" ) 
        
  
    
