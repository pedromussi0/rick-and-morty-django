import requests
from django.core.management.base import BaseCommand

from App.models import Character


class Command(BaseCommand):
    help = "Fetch data from API and save to DB"

    def handle(self, *args, **options):
        api_url = 'https://rickandmortyapi.com/api/character'
        page = 1
        while True:
            response = requests.get(api_url, params={'page': page})
            if response.status_code != 200:
                break
            data = response.json()
            for character_data in data['results']:
                # Extract the character's photo URL from the API response

                # Check if the character already exists in the database
                character, created = Character.objects.get_or_create(
                    id=character_data['id'],
                    defaults={
                        'name': character_data['name'],
                        'status': character_data['status'],
                        'species': character_data['species'],
                        'type': character_data['type'],
                        'gender': character_data['gender'],
                        'image': character_data['image']
                    }
                )

                # If the character already exists, update its fields with the latest data
                if not created:
                    character.name = character_data['name']
                    character.status = character_data['status']
                    character.species = character_data['species']
                    character.type = character_data['type']
                    character.gender = character_data['gender']
                    character.image = character_data['image']
                    character.save()
            page += 1
        self.stdout.write(self.style.SUCCESS("DADOS SALVOS NA DB!"))