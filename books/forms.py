from django import forms
from books.models import BooksApp
from django.contrib.auth.models import User


class BooksAppForm(forms.Form):
    name=forms.CharField()
    author=forms.CharField()
    review=forms.CharField()
    price=forms.IntegerField()
    publisheddate=forms.DateField()

class BooksAppModelForm(forms.ModelForm):
   class Meta:
        model=BooksApp
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "author":forms.TextInput(attrs={"class":"form-control"}),
            "reviews":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "publisheddate":forms.DateInput(attrs={"class":"form-control"}),

        }

class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username","email","password"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    
