from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import StudentDetails, ProductDetails
from django.contrib.auth.models import User
from .forms import CustomerRegistrationForm, ProductRegistrationForm

from django.contrib import messages


# Create your views here.
def product(request):
    return render(request,'product.html')
def customer (request):
    all= StudentDetails.objects.all
    return render(request,'customer.html',{'all':all})
def show_customer (request):
    all= StudentDetails.objects.all
    return render(request,'show_customer.html',{'all':all})

def show_product (request):
    all= ProductDetails.objects.all
    return render(request,'show_product.html',{'all':all})

# from django.shortcuts import render
# from .models import MyModel,StudentDetails, ProductDetails
# from .forms import MyForm

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'customer.html', {'form': form})



def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            customer = StudentDetails()
            cd = form.cleaned_data
            customer.fname = cd['fname']
            customer.lname = cd['lname']
            customer.addr = cd['addr']
            customer.birthdate = cd['birthdate']
            customer.tel = cd['tel']
            customer.save()
            messages.success(request, 'customer registered successfully', 'succes')
            return redirect('http://mandn.pythonanywhere.com/home/showcustomer/')
    else:

        form = CustomerRegistrationForm()
    return render(request, 'customer.html', {'form':form})




def product_register(request):
    if request.method == 'POST':
        form = ProductRegistrationForm(request.POST)
        if form.is_valid():
            product = ProductDetails()
            cd = form.cleaned_data
            product.name = cd['name']
            product.category = cd['category']
            product.price = cd['price']
            product.features = cd['features']
            product.description = cd['description']

            product.save()
            messages.success(request, 'product registered successfully', 'succes')
            return redirect('http://mandn.pythonanywhere.com/home/')
    else:
        print("gggggggg")
        form = ProductRegistrationForm()
    return render(request, 'product.html', {'form':form})
# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})



def my_form_products(request):
  if request.method == "POST":
    form = MyForm_products(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm_products()
  return render(request, 'products.html', {'form': form})



#store
def store(request):
	all = ProductDetails.objects.all
	return render(request, 'store/store.html', {'all':all})

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

# def login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})