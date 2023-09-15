from django.db import models


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="") 

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30)
    timestamp = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.email
    
    
