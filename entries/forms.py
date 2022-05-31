from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  
from .models import Media, Entry
from profiles.models import Tag
from django.forms import ModelForm, Textarea



class EntryForm(ModelForm):
    FINISHED = 'FINISHED'
    STARTED = 'STARTED'
    WISHLIST = 'WISHLIST'
    QUIT = 'QUIT'
    STATUS_CHOICES  = [(WISHLIST, 'Wish List'), (QUIT, 'Quit')]
    tags            = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    source          = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={"placeholder": "library, kindle, netflix, etc",}))
    rating          = forms.DecimalField(initial=0.00)
    my_comment      = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5,"cols":40,}),)
    review          = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 10,"cols":40}),)
    recommended_by  = forms.CharField(required=False)
    status          = forms.CharField(required=False, widget=forms.RadioSelect(choices=STATUS_CHOICES),initial='WISHLIST' )
    date_started    = forms.DateField(required=False, widget=forms.DateInput(format='%m/%d/%Y',attrs={"placeholder":"mm/dd/yyyy"}),)
    date_finished   = forms.DateField(required=False, widget=forms.DateInput(format='%m/%d/%Y',attrs={"placeholder":"mm/dd/yyyy"}))

    def __init__(self, *args, **kwargs):
        # Grants access to the request object so that only tags of the current user
        # are given as options
        self.userId = kwargs.pop('userId')
        super(EntryForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.filter(user=self.userId)


    class Meta:
        model = Entry
        fields = ['user','media','tags','source','rating','my_comment', 'review', 'recommended_by', 'status','date_started','date_finished',]

    

