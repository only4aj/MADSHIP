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
    details = models.CharField(max_length=1000)
    description = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images',width_field="width")
    width = models.IntegerField()

    def __str__(self) -> str:
        return self.title