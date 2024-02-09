from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication


from api.serializers import UserSerializer,ProductSerializer,CartSerializer,OrderSerializer,ReviewSerializer
from api.serializers import Product,Cart,Order,Review,Address
# Create your views here.


class ListUsersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class CreateUserAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UpdateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request, user_id, format=None):
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    @action(methods=['POST'],detail=True)
    def add_to_cart(self,request,*args,**kwargs):
        serializer= CartSerializer(data=request.data)
        product_obj=Product.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(product=product_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    @action(methods=['POST'],detail=True)
    def place_order(self,request,*args,**kwargs):
        serializer=OrderSerializer(data=request.data)
        product_obj=Product.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(product=product_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    @action(methods=['POST'],detail=True)
    def add_review(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        product_obj=Product.objects.get(id=kwargs.get('pk'))
        user=request.user
        if serializer.is_valid():
            serializer.save(product=product_obj,user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    

class CartsView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=CartSerializer
    queryset=Cart.objects.all()

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)   
    
class OrdersView(viewsets.GenericViewSet,mixins.ListModelMixin):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
# addresses/views.py
from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
