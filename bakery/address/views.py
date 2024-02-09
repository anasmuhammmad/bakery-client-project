from django import forms
from django.http import HttpResponse

# class AddressForm(forms.Form):
#     recipient_name = forms.CharField(max_length=100)
#     recipient_address = forms.CharField(max_length=255)
#     landmark = forms.CharField(max_length=100)
#     recipient_phone = forms.CharField(max_length=15)
#     ADDRESS_TYPE_CHOICES = [
#         ('home', 'Home'),
#         ('office', 'Office'),
#         ('other', 'Other'),
#     ]
#     address_type = forms.ChoiceField(choices=ADDRESS_TYPE_CHOICES)

# def address_list(request):
#     # Your view logic here
#     return HttpResponse("Address list view")

# def address_create(request):
#     # Your view logic here
#     return HttpResponse("Address create view")