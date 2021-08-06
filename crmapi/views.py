from django.db.models.base import Model
from django.http import request
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import auth
from django.contrib.auth import login,logout,authenticate
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET'])
def home(request):
    return Response('Crm')

@api_view(["GET"])
def logout_user(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return Response('User Logged out successfully')
    else:
        return Response('No users logged in')
 
import json

@api_view(["POST"])
def login_user(request):
    reqBody = json.loads(request.body)
    email1 = reqBody['email']
    password = reqBody['password']
    try:
        ac = User.objects.get(email=email1)
        if ac.password == password:    
            data = {}
            auth.login(request, ac)
            data["message"] = "user logged in"
            data["email"] = ac.email
            Res = {"data": data}
            return Response(Res)
        else:
            return Response('Invalid Login')
    except Exception as e:
        return Response(e)


class Enquiry_claim(generics.RetrieveUpdateAPIView):

    model = Enquiry_Form
    serializer_class = Enquiry_UpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enquiry_Form.objects.filter(claimed_by__isnull=True)

    def perform_update(self, enquiry):
        enquiry.instance.claimed_by = self.request.user
        enquiry.save()
        

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
    

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def EnquiriesUpdate(request,pk):
#     try:
#         adata = Enquiry_Form.objects.get(id=pk)
#         if adata.claimed_by == request.user:
#             return Response('You claimed this Before!')
#         else:
#             data = Enquiry_Form.objects.filter(claimed_by__isnull=True).get(id=pk)
#             data.claimed_by = request.user
#             data.save()
#             return Response('Successfully Claimed')
#     except ObjectDoesNotExist as Doesnotexist:
#         return Response('Enquiry Doesnot exist')

