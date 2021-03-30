from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.

ITEM_CATEGORY = [
    ['stationery', 'Stationery'],
    ['vegetable', 'Vegtables/Fruits'],
    ['pantry', 'Pantry'],
    ['personalcare','Personalcare'],
    ['cleaning','Cleaning'],
    ['beverges','Beverges'],
    ['packagedfood','Packagedfood'],
    ['cookingessential','Cookingessential'],
    ['topoffer','Topoffer'],
    ['todaydeal','Todaydeal'],
    ['fruit','Fruit'],
    ['toy','Toy'],
    ['school','School'],
    ['spices','Spices'],
    ['houseware','Houseware'],


]
class PoductDetails(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.CharField(max_length = 5)
    price = models.CharField(max_length=6)
    brandname = models.CharField(max_length=30)
    itemweight = models.CharField(max_length=10)
    about = models.CharField(max_length=250)
    discount = models.CharField(blank = True, max_length= 5, null = True)
    product_image = models.ImageField()


    category = models.CharField(choices=ITEM_CATEGORY, max_length=17, null = True , blank = True)

    def __str__(self):
        return self.name+'-'+self.price

class userDetail(models.Model):
    mobile_number = models.CharField(max_length=10, null = True, blank = True)
    address = models.CharField(max_length = 1000, null = True, blank = True)
    pincode = models.CharField(max_length= 6,null  = True, blank = True)
    user = models.OneToOneField(User, null = True, blank = True, on_delete=models.CASCADE)

class cart(models.Model):
    user = models.ForeignKey(userDetail, on_delete=models.CASCADE)
    product = models.ForeignKey(PoductDetails, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10, default=1)

class usercheck(models.Model):
    total = models.CharField(max_length=1000, default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class address(models.Model):
    name = models.CharField(max_length=10, null = True, blank = True)
    mobile_number = models.CharField(max_length=10, null = True, blank = True)
    address = models.CharField(max_length = 1000, null = True, blank = True)
    pincode = models.CharField(max_length= 6,null  = True, blank = True)



