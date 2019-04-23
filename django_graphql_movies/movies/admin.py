from django.contrib import admin
from django_graphql_movies.movies.models import Actor, Movie

# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
