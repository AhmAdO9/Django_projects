# Generated by Django 4.1.7 on 2023-05-14 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_daily_rate_remove_movie_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_year',
        ),
    ]