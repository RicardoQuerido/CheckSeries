from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests
from app.forms import UserCreateForm
from . import config


def index(request):
    resp = requests.get(
        'https://api.themoviedb.org/3/tv/popular?api_key=' + config.api_key + '&language=en-US&page=1')
    if resp.status_code != 200:
        print("SOMETHING WENT WRONG!")
    shows = resp.json()["results"][:3]
    return render(request, 'index.html', {'shows': shows})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid() and not User.objects.filter(email=form.data["email"]):
            username = form.data["username"]
            password = form.data["password1"]
            form.save()
            request_user = authenticate(request, username=username, password=password)
            login(request, request_user)
            return redirect('/')
        else:
            return render(request, 'sign_up.html', {'form': form, 'email_error': True})
    else:
        form = UserCreateForm()
    return render(request, 'sign_up.html', {'form': form})


def tv_show(request, id):
    resp = requests.get(
        'https://api.themoviedb.org/3/tv/' + str(id) + '?api_key=' + config.api_key + '&language=en-US')
    if resp.status_code != 200:
        print("SOMETHING WENT WRONG!")

    show = resp.json()

    return render(request, 'tv_show.html', {'show': show})
