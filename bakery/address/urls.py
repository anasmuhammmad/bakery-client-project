from django.urls import path
from . import views




urlpatterns = [
    path('list/', views.AddressListCreateView.as_view(), name='address_list'),
    path('create/', views.AddressListCreateView.as_view(), name='address_create'),


]


