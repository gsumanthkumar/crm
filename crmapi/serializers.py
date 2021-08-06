from django.db.models import fields
from rest_framework import serializers
from .models import *

class Enquiry_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enquiry_Form
        fields = ['id','name','email','course_interest','description']

class Enquiry_UpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enquiry_Form
        fields = '__all__'
        read_only_fields = ('name', 'email','course_interest',
                            'description', 'claimed_by')