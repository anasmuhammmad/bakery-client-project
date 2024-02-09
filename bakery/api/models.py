from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Occasion(models.Model):
    name=models.CharField(max_length=200,unique=True)
    
    def __str__(self) -> str:
        return self.name
    

  

class Product(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    weight=models.CharField(max_length=200,default="1kg")
    price=models.FloatField()
    image=models.ImageField(upload_to='media/image',blank=True,null=True)
    

    def __str__(self) -> str:
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    statusoptions=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=statusoptions,default="in-cart")
    qty=models.PositiveIntegerField()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    address=models.CharField(max_length=300)
    matter=models.CharField(max_length=200)

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(max_length=200)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])
   


    def __str__(self) -> str:
        return self.comment
    



class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='api_addresses')
    recipient_name = models.CharField(max_length=255)
    recipient_address = models.CharField(max_length=512)
    landmark = models.CharField(max_length=255)
    recipient_phone = models.CharField(max_length=15)
    
    ADDRESS_TYPE_CHOICES = [
        ('home', 'Home'),
        ('office', 'Office'),
        ('other', 'Other'),
    ]
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)

    def __str__(self):
        return f"{self.recipient_name}'s {self.address_type} address"

