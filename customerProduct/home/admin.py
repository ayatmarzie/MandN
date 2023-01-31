from django.contrib import admin
from .models import StudentDetails, MyModel,products, ProductDetails, Cart, CartItem
# Register your models here.


admin.site.register(StudentDetails)
admin.site.register(ProductDetails)
admin.site.register(products)
admin.site.register(MyModel)

admin.site.register(Cart)
admin.site.register(CartItem)