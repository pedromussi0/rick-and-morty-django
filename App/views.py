import requests
from django.shortcuts import render, get_object_or_404
from App.models import Character, Episodes


def home(request):
    characters = Character.objects.all()
    return render(request, "home.html", {"characters": characters})


def detail_view(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    context = {
        'character': character,
        'gender': character.gender,
        'status': character.status,
        'species': character.species,
        'type': character.type,
    }
    return render(request, 'detail.html', context)


def episode_list(request):
    episodes = Episodes.objects.all()
    context = {
        'episodes': episodes,
    }
    return render(request, 'episode_list.html', context)


def episode_detail(request, episode_id):
    episode = get_object_or_404(Episodes, id=episode_id)
    characters = episode.characters.all()
    context = {'episode': episode, 'characters': characters}
    return render(request, 'episode_detail.html', context)
