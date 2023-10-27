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

    def __str__(self) -> str:
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
