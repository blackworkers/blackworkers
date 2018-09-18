from django.urls import path
from artists import views


urlpatterns = [
    # A view function that will be called if the URL pattern is detected: views.index,  which is the function named index() in the views.py file.
    path('', views.index, name='index'),
    path('artist_list/', views.ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
    path('us_artist_list/', views.USArtistListView.as_view(), name='us-artist-list'),
]
