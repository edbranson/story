from django import forms

from django.contrib.auth.models import User  
from .models import Media
from django.forms import ModelForm, Textarea



class MediaForm(ModelForm):
    TEXT = 'TEXT'
    VIDEO = 'VIDEO'
    AUDIBLE = 'AUDIBLE'
    MEDIA_CHOICES = [(TEXT, 'Text'), (VIDEO, 'Video'), (AUDIBLE, 'Audible')]
    media_type   = forms.CharField(required=False, widget=forms.RadioSelect(choices=MEDIA_CHOICES) )
    author_link  = forms.URLField(empty_value="google.com")
    ave_rating  = forms.DecimalField(required=False)

    class Meta:
        model = Media
        fields = ['title','author','actors','published','subject', 'reader', 'media_type', 'audience','promo_img','promo_desc','author_link', 'series','ave_rating']
        widgets = {
            'promo_desc': Textarea,
        }

class MediaSearchForm(ModelForm):
    TEXT = 'TEXT'
    VIDEO = 'VIDEO'
    AUDIBLE = 'AUDIBLE'
    MEDIA_CHOICES = [(TEXT, 'Text'), (VIDEO, 'Video'), (AUDIBLE, 'Audible')]

    class Meta:
        model = Media
        fields = ['title', 'media_type']