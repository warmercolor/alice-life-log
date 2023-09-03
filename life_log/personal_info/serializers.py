from rest_framework import serializers
from .models import Personal, Hobby, Book, Movie


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class PersonalSerializer(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True, read_only=True)
    favorite_books = BookSerializer(many=True, read_only=True)
    favorite_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Personal
        fields = "__all__"
