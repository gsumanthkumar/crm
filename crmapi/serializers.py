from rest_framework import serializers
from .models import *

class Enquiry_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enquiry_Form
        fields = ['id','name','email','course_interest','description']