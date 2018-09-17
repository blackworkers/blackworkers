from django.contrib import admin

# Register your models here.
from artists.models import ArtistsRaw

# admin.site.register(ArtistsRaw)
# Define the admin class
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('instagram_handle', 'likes', 'city', 'state')

# Register the admin class with the associated model
admin.site.register(ArtistsRaw, ArtistAdmin)
