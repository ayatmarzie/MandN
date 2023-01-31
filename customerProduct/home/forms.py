from django import forms
from .models import StudentDetails,products



from django import forms
from .models import StudentDetails, ProductDetails

# class MyForm(forms.ModelForm):
#   class Meta:
#     model = StudentDetails
#     fields = ["fname", "lname","birthdate","addr"]
#     labels = {"fname": "First Name","lname": "Last Name","birthdate":"Birth Date","addr":"Address"}
#



class CustomerRegistrationForm(forms.Form):
    # idno = models.IntegerField(primary_key=True)
    # class Meta:
    #     model = StudentDetails
    #     fields = ["fname", "lname","birthdate","addr", "tel"]
    #     labels = {"fname": "fname","lname": "lname","birthdate":"birthdate","addr":"addr", "tel": "tel"}

    fname = forms.CharField()
    lname = forms.CharField()
    addr = forms.CharField()
    birthdate = forms.DateField()
    tel = forms.IntegerField()


class ProductRegistrationForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()
    price = forms.IntegerField()
    features = forms.CharField()
    description = forms.CharField()


# class LoginForm(forms.ModelForm):
#   class Meta:
#     model = StudentDetails
#     fields = ["username", "password"]
#     labels = {"fname": "UserName", "password": "password"}


class MyForm(forms.ModelForm):
  class Meta:
    model = StudentDetails
    fields = ["fname", "lname","birthdate","addr"]
    labels = {"fname": "First Name","lname": "Last Name","birthdate":"Birth Date","addr":"Address"}
class MyForm_products(forms.ModelForm):
  class Meta:
    model = products
    fields = ["name", "group","Price","features","details"]
    labels = {"name": "name","group": "group","features":"features","details":"details"}

# class LoginForm(forms.ModelForm):
#   class Meta:
#     model = StudentDetails
#     fields = ["username", "password"]
#     labels = {"fname": "UserName", "password": "password"}
