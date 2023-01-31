from django.db import models
from django.contrib.auth.models import User

Car_CHOICES = (
    ('Volvo', 'Volvo'),
    ('Saab', 'Saab'),
    ('Flat', 'Flat'),
    ('Audi', 'Audi'),

)


class StudentDetails(models.Model):
    #idno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=33)
    lname = models.CharField(max_length=33)
    addr = models.CharField(max_length=200)
    birthdate = models.DateField()
    tel = models.IntegerField()

class ProductDetails(models.Model):
    #idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=33)
    category = models.CharField(max_length=33)
    price = models.IntegerField()
    features = models.CharField(max_length=200)
    description = models.CharField(max_length=200)



class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()
# Create your models here.



class products(models.Model):
    name = models.CharField(max_length=33)
    group = models.CharField(max_length=6, choices=Car_CHOICES, default='Volvo')
    Price=models.IntegerField()
    features=models.CharField(max_length=100)
    details=models.CharField(max_length=330)



# Create your models here.
# class Product(models.Model):
#     title = models.CharField(max_length=150)
#     description = models.TextField()
#     price = models.PositiveBigIntegerField()
#     image = models.ImageField()
#
#     def __str__(self):
#         return self.title
#
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_paid = models.BooleanField(default=False)
#
#     @property
#     def total_price(self):
#     total = 0
#     for cart_item in self.cartitems.all():
#          total += (cart_item.price * cart_item.quantity)
#     return int(total)
#
#     def __str__(self):
#     return self.user.username
#
#
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
#                              related_name='cartitems')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     price = models.PositiveIntegerField()
#     quantity = models.PositiveSmallIntegerField()
#
#     @property
#     def total_price(self):
#         return int(self.price * self.quantity)
#
#     def __str__(self):
#         return self.product.title


class Cart(models.Model):
    user = models.ForeignKey(StudentDetails, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

    @property
    def total_price(self):
        total = 0
        for cart_item in self.cartitems.all():
             total += (cart_item.price * cart_item.quantity)
        return int(total)

        def __str__(self):
             return self.user.fname


class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
     related_name='cartitems')
     product = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
     price = models.PositiveIntegerField()
     quantity = models.PositiveSmallIntegerField()

     @property
     def total_price(self):
          return int(self.price * self.quantity)

     def __str__(self):
          return self.product.title