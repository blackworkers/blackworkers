from django.db import models
from django.urls import reverse

# Create your models here.
class ArtistsRaw(models.Model):
    """Model representing a book genre."""
    instagram_handle = models.CharField(max_length=200, help_text='Enter an artists instagram handle')
    caption = models.CharField(max_length=5000, help_text='Enter the artists post caption')
    shortcode = models.CharField(max_length=200, help_text='Enter the posts shortcode')
    city = models.CharField(max_length=200, help_text='Enter the artists city')
    state = models.CharField(max_length=200, help_text='Enter the artists state')
    likes = models.IntegerField()
    display_url = models.URLField(max_length=500)

    def get_absolute_url(self):
        return reverse('artist-detail', args=[str(self.id)])


    def __str__(self):
        """String for representing the Model object."""
        return self.instagram_handle
