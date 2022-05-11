from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from .models import Profile, Tag
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2',]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'name_first', 'name_last', 'cell_phone', 'email', 'profile_image',]
        
class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['user', 'description',]