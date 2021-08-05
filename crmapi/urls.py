from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('enquiries/',views.EnquiriesList.as_view(),name='enquiries'),
    path('enquiries/claim/<int:pk>',views.EnquiriesUpdate,name='claim'),
    path('enquiries/claimed',views.Claimed_Enquiries.as_view(),name='claimedenquiries')
]