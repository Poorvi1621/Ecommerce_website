from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES=(
('CR','Curd'),
('ML','Milk'),
('LS','Lassi'),
('MS','Milkshake'),
('PN','Paneer'),
('GH','Ghee'),
('CZ','Cheese'),
('IC','Ice-Creams'),
)



class Product(models.Model):
     title=models.CharField(max_length=100)
     selling_price = models.FloatField()
     discounted_price = models.FloatField()
     description =models.TextField()
     composition =models.TextField(default='')
     prodapp=models.TextField(default='')
     category =models.CharField( choices=CATEGORY_CHOICES,max_length=2)
     product_image=models.ImageField(upload_to='product')
     def __str__(self):
             return self.title
     

STATE_CHOICES = (
('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
('Andra Pradesh', 'Andra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chhattisgarh', 'Chhattisgarh'),
('chandigarh', 'chandigarh'),
('dadra & Nagar Haveli', 'dadra & Nagar Haveli'),
('Delhi', 'Delhi'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Utter Pradesh', 'Utter Pradesh'),
('Andra Pradesh', 'Andra Pradesh'),
('Mumbai', 'Mumbai'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'), )   

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def __str__(self):
        return str(self.id)
         