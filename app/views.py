from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    resp = requests.get(
        'https://api.themoviedb.org/3/tv/popular?api_key=2bbd9e8844b9e73b0fb2e47e0f6d3b88&language=en-US&page=1')
    if resp.status_code != 200:
        print("SOMETHING WENT WRONG!")
    shows = resp.json()["results"][:3]
    return render(request, 'index.html', {'shows': shows})
