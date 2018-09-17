from django.urls import path
from artists import views


urlpatterns = [
    # A view function that will be called if the URL pattern is detected: views.index,  which is the function named index() in the views.py file.
    path('', views.index, name='index'),
    path('artist_list/', views.ArtistListView.as_view(), name='artist_list'),
    path('book/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
]
