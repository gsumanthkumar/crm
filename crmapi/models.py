from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .managers import *



class User(AbstractUser):
    """User model."""

    username = None
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Enquiry_Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    course_interest = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    claimed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='userclaimedenquiries')

    def __str__(self):
        return self.course_interest