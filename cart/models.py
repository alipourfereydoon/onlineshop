from django.db import models
from account.models import User
from product.models import Product

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User , on_delete= models.CASCADE , related_name='orders')
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE , related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='items')
    size = models.CharField(max_length=12)
    color = models.CharField(max_length=12)
    quantity = models.IntegerField()
    price = models.IntegerField()

class DiscountCode(models.Model):
    name = models.CharField(max_length=20, unique=True)
    discount = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
    


    




