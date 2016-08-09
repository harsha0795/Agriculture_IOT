from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Sensor

class SignupForm(UserCreationForm):
    """docstring for SuigupForm. This class is used to create a signup form with email, password, first and last name"""
    email = forms.EmailField(required=True)
    first_name = forms.CharField( max_length=100, required=True)
    last_name = forms.CharField(required=True)
    class Meth:
	    model = User
	    fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            print "Saving user"
            user.save()
        return user

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ('Sensor_name',)
    user =""




