from django.db import models
from django.urls import reverse

# Create your models here.
class ArtistsRaw(models.Model):
    """Model representing a book genre."""
    shortcode = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    caption = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    display_url = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    loc_name = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    loc_lat = models.IntegerField(default='0', null=True)
    loc_long  = models.IntegerField(default='0', null=True)
    instagram_handle = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    likes = models.IntegerField(default='0', null=True)
    city = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    state = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    country = models.CharField(max_length=5000, help_text='Enter the artists post caption', blank=True, null=True)
    rejected = models.BooleanField(default=False, null=True)
    taken_at_ts = models.DateTimeField(null=True)


    def __str__(self):
        """String for representing the Model object."""
        return self.instagram_handle
