from django.db import models

from profiles.models import Profile, Tag


# Create your models here.
class Media(models.Model):
    TEXT = 'TEXT'
    VIDEO = 'VIDEO'
    AUDIBLE = 'AUDIBLE'
    MEDIA_CHOICES = [(TEXT, 'Text'), (VIDEO, 'Video'), (AUDIBLE, 'Audible')]

    RATING_CHOICES = [(0, 0), (1, 1), (2, 2), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    actors = models.CharField(max_length=200, blank=True)
    published = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=30, blank=True)
    reader = models.CharField(max_length=100, blank=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES)
    audience = models.CharField(max_length=30, blank=True)
    promo_img = models.ImageField(blank=True)
    promo_desc = models.TextField(max_length=10000, blank=True)
    author_link = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    ave_rating = models.DecimalField(decimal_places=2, max_digits=3, choices=RATING_CHOICES, blank=True, null=True)
    series = models.CharField(max_length=100, blank=True)
    

    def __str__(self):
        return str(self.title)

