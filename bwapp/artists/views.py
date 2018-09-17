from django.shortcuts import render
from django.views import generic

# Create your views here.
from artists.models import ArtistsRaw

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_artists = ArtistsRaw.objects.all().count()

    context = {
        'num_artists': num_artists,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = ArtistsRaw

class ArtistListView(generic.ListView):
    model = ArtistsRaw
    context_object_name = 'artist_list'   # your own name for the list as a template variable
    queryset = ArtistsRaw.objects.order_by('-likes') # Get 5 books containing the title war
    paginate_by = 9
    #template_name = 'artists/artist_list.html'  # Specify your own template name/location

class ArtistDetailView(generic.DetailView):
    model = ArtistsRaw
    context_object_name = 'artist_detail'
