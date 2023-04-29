import django.forms
from django.db import models


class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, default="Unknown")
    status = models.CharField(max_length=200, default="Unknown")
    species = models.CharField(max_length=200, default="Unknown")
    type = models.CharField(max_length=200, default="Unknown")
    gender = models.CharField(max_length=200, default="Unknown")
    image = models.URLField(max_length=200, default="https://rickandmortyapi.com/api/character/avatar/unknown.jpeg")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.image:
            self.image = f"https://rickandmortyapi.com/api/character/avatar/{self.id}.jpeg"
        super().save(*args, **kwargs)