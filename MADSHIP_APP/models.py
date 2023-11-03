from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=30)
    PNumber = models.PositiveBigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username

class ProductItem(models.Model):
    brand = models.CharField(max_length=20)
    title = models.CharField(max_length=500)
    dis_price = models.IntegerField()
    act_price = models.IntegerField()
    offer = models.IntegerField()
    item_id = models.IntegerField()
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images',width_field="width")
    width = models.IntegerField(default=0)
    d1 = models.CharField(max_length=50,default=0)
    d2 = models.CharField(max_length=50,default=0)
    d3 = models.CharField(max_length=50,default=0)
    d4 = models.CharField(max_length=50,default=0)

    def __str__(self) -> str:
        return self.title
    
class customerdetail(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=500, null=True, blank=True)
    mail = models.EmailField()
    mobile = models.PositiveBigIntegerField()
    pincode = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name