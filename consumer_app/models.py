from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=10)
    pic = models.ImageField(default='user.jpg',upload_to='consumer_pics')
    about_me = models.TextField(null=True)
    
    
    def __str__(self) -> str:
        return self.name
    
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=150)
    des = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places= 2, default=500)
    pic = models.FileField(upload_to='products_images', default='sad.jpg')
    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    
class Cart(models.Model):
    email = models.EmailField() 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    image = models.ImageField(null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places= 2, default=0)
    
    def __str__(self) -> str:
        return str(self.email)


class CartHistory(models.Model):
    email = models.EmailField() 
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    image = models.ImageField(null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places= 2, default=0)
    
    def __str__(self) -> str:
        return str(self.email)

