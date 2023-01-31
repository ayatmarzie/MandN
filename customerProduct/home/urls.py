from django.urls import path
from . import views
urlpatterns = [
    path('customer/', views.customer_register ),
    path('product/',views.product_register),
    path('showcustomer/',views.show_customer),
    path('showproduct/',views.show_product),
    path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path(r'form', views.my_form, name='form')
    # path(r'login', views.my_form, name='form')
]
