# Generated by Django 4.2 on 2023-04-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_remove_character_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.ImageField(default='Unknown', max_length=200, upload_to=''),
        ),
    ]
