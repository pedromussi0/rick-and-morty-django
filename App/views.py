from django.shortcuts import render, get_object_or_404
from App.models import Character


def home(request):
    character_list = Character.objects.all()
    return render(request, "home.html", {"characters": character_list})


def detail_view(request, character_id):
    character = get_object_or_404(Character, id=character_id)
    context = {'character': character}
    return render(request, 'detail.html', context)
