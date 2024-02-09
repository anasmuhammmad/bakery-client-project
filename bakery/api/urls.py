
from django.urls import path,include
from .views import AddressListCreateView

from .views import ListUsersAPIView,CreateUserAPIView,RetrieveUserAPIView,UpdateUserAPIView


urlpatterns = [
  path('users/', ListUsersAPIView.as_view(), name='list-users'),
  path('users/create/', CreateUserAPIView.as_view(), name='create-user'),
  path('users/<int:user_id>/', RetrieveUserAPIView.as_view(), name='retrieve-user'),
  path('users/<int:user_id>/update/', UpdateUserAPIView.as_view(), name='update-user'),
  path('address/', AddressListCreateView.as_view(), name='address-list-create'),
  # path('uploadimage',views.uploadimage,name='uploadimage')
  

]

