from django.shortcuts import render, redirect
import requests
from app.forms import UserCreateForm
from . import config


def index(request):
    resp = requests.get(
        'https://api.themoviedb.org/3/tv/popular?api_key=' + config.api_key + '&language=en-US&page=1')
    if resp.status_code != 200:
        print("SOMETHING WENT WRONG!")
    shows = resp.json()["results"]
    return render(request, 'index.html', {'shows': shows})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreateForm()
    return render(request, 'sign_up.html', {'form': form})
