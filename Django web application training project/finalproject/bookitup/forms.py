from django import forms
from .models import book
from .models import Login
from .models import Register
forms.ModelForm
class Meta:
        model=book

class bookingform(forms.Form):

        First = forms.CharField()
        Last = forms.CharField()
        Phone = forms.IntegerField()
        Email = forms.CharField()
        Arriving = forms.DateField()
        Departure = forms.DateField()
        adults = forms.IntegerField()
        children = forms.IntegerField()
        questions = forms.CharField()
class LoginForm(forms.Form):
        Username = forms.CharField()
        Password = forms.CharField()
        class Meta:
                model=Login
                fields=('Username','Password',)
class RegisterForm(forms.Form):
        uname = forms.CharField()
        uemail=forms.CharField()
        upassword = forms.CharField()
        ure_password=forms.CharField()
        class Meta:
                model=Register
                fields=('uname','uemail','upassword','ure_password')

