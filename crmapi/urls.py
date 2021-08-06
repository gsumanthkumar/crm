from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('userlogin/',views.login_user,name='userlogin'),
    path('userlogout/',views.logout_user,name='userlogout'),
    path('enquiries/',views.EnquiriesList.as_view(),name='enquiries'),
    path('enquiries/claim/<int:pk>',views.Enquiry_claim.as_view(),name='claim'),
    path('enquiries/claimed',views.Claimed_Enquiries.as_view(),name='claimedenquiries')
]