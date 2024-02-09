from django.contrib.auth.models import User
from api.models import Product,Cart,Order,Review,Address

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self, validated_data):
        return  User.objects.create_user(**validated_data)  
    
class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    Product=serializers.CharField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    reviews= ReviewSerializer(read_only=True,many=True)

    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=ProductSerializer(read_only=True)
    date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    # qty=serializers.CharField(read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=ProductSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street_address', 'city', 'state', 'zip_code','phone','country']

        