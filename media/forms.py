from django import forms

from django.contrib.auth.models import User  
from .models import Media
from django.forms import ModelForm, Textarea



class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ['title','author','actors','published','subject', 'reader', 'media_type', 'audience','promo_img','promo_desc','author_link', 'series',]
        widgets = {
            'promo_desc': Textarea,
        }
