# Generated by Django 4.2 on 2023-04-27 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Unknown', max_length=200)),
                ('status', models.CharField(default='Unknown', max_length=200)),
                ('species', models.CharField(default='Unknown', max_length=200)),
                ('type', models.CharField(default='Unknown', max_length=200)),
                ('gender', models.CharField(default='Unknown', max_length=200)),
            ],
        ),
    ]