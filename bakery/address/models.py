from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# class Address(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipient_name = models.CharField(max_length=255)
#     recipient_address = models.CharField(max_length=512)
#     landmark = models.CharField(max_length=255)
#     recipient_phone = models.CharField(max_length=15)
    
#     ADDRESS_TYPE_CHOICES = [
#         ('home', 'Home'),
#         ('office', 'Office'),
#         ('other', 'Other'),
#     ]
#     address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)

#     def __str__(self):
#         return f"{self.recipient_name}'s {self.address_type} address"