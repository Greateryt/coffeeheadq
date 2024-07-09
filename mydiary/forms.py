from django import forms
from .models import Diary
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields  = ['text','photo']

class UserRegistrationForm(UserCreationForm):
        email = forms.EmailField
        class Meta:
            model = User
            fields = ('email','username','password1','password2')