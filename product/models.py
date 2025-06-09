from django.db import models

# Create your models here


    

class Size(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title
    
class Color(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title   
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.SmallIntegerField()
    image = models.ImageField(upload_to='products')
    size = models.ManyToManyField(Size ,blank=True , null=True , related_name='products')
    color = models.ManyToManyField(Color , related_name='color')

    def __str__(self):
        return self.title
    
    
    
class information(models.Model):
    product = models.ForeignKey(Product, null=True , on_delete= models.CASCADE , related_name= 'informations')
    text = models.TextField()

    def __str__(self):
        return self.text[:20]
    