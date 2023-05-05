from django.core.management.base import BaseCommand
import requests
import json
from App.models import Episodes


class Command(BaseCommand):
    help = 'Populates the database with episodes from the Rick and Morty API'

    def handle(self, *args, **options):
        url = 'https://rickandmortyapi.com/api/episode'
        all_episodes = []

        # Make a GET request to the /episode endpoint of the API for each page of episodes
        while url:
            response = requests.get(url)

            # Convert the response data to a Python dictionary
            data = json.loads(response.content)

            # Append the list of episodes to the list of all episodes
            all_episodes.extend(data['results'])

            # Get the URL of the next page of episodes, or None if there are no more pages
            url = data['info']['next']

        # Loop through the list of episodes and create an Episode object for each one
        for episode_data in all_episodes:
            episode, created = Episodes.objects.get_or_create(
                id=episode_data['id'],
                defaults={
                    'name': episode_data['name'],
                    'episode': episode_data['episode']
                }
            )

            if created:
                # Extract the list of character URLs and convert them to a list of IDs
                character_ids = [int(url.split('/')[-1]) for url in episode_data['characters']]

                # Add the character IDs to the episode's "characters" field using the "add" method
                episode.characters.add(*character_ids)

        self.stdout.write(self.style.SUCCESS('Episodes successfully populated'))