from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    # Movie.objects.filter(release_year = 1989)
    # Movie.objects.get(id=1)
    return render(request, 'movies/index.html', {'movies': movies})



def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', {'movie':movie})