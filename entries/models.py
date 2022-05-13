from django.db import models
from django.contrib.auth.models import User
from media.models import Media
from profiles.models import Profile, Tag

# Create your models here.


class Entry(models.Model):
    FINISHED = 'FINISHED'
    STARTED = 'STARTED'
    WISHLIST = 'WISHLIST'
    QUIT = 'QUIT'
    STATUS_CHOICES = [(FINISHED, 'Finished'), (STARTED, 'Started'), (WISHLIST, 'Wish List'), (QUIT, 'Quit')]
 
    RATING_CHOICES = [(0, 0), (1, 1), (2, 2), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    media = models.ForeignKey(Media, on_delete=models.CASCADE, default="")
    tags = models.ManyToManyField(Tag)
    source = models.CharField(max_length=25, blank=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, choices=RATING_CHOICES)
    my_comment = models.CharField(max_length= 100, blank=True)
    review = models.TextField(max_length=2000, blank=True)
    recommended_by = models.CharField(max_length=30, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date_started = models.DateField(null=True)
    date_finished = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)

