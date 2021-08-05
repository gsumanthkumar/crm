from django.http import request
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response('Crm')


class EnquiriesList(generics.ListAPIView):

    model = Enquiry_Form
    serializer_class = Enquiry_Serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enquiry_Form.objects.filter(claimed_by__isnull=True)

class Claimed_Enquiries(generics.ListAPIView):

    model = Enquiry_Form
    serializer_class = Enquiry_Serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enquiry_Form.objects.filter(claimed_by = self.request.user)
    

@api_view(['GET'])
def EnquiriesUpdate(request,pk):
    try:
        adata = Enquiry_Form.objects.get(id=pk)
        if adata.claimed_by == request.user:
            return Response('You claimed this Before!')
        else:
            data = Enquiry_Form.objects.filter(claimed_by__isnull=True).get(id=pk)
            data.claimed_by = request.user
            data.save()
            return Response('Successfully Claimed')
    except ObjectDoesNotExist as Doesnotexist:
        return Response('Enquiry Doesnot exist')

