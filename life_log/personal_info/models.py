from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Personal(Timestamped):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    hometown = models.CharField(max_length=100)
    hobbies = models.ManyToManyField("Hobby")
    favorite_books = models.ManyToManyField("Book")
    favorite_movies = models.ManyToManyField("Movie")


class Hobby(Timestamped):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Book(Timestamped):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)


class Movie(Timestamped):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
