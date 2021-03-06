from django.shortcuts import render
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class MoviesView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context = {'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id):
        movie = self.get_object(id)
        movie.delete()
        serializer = MovieSerializer(movie, context = {'request': request})
        return Response(serializer.data)

    def delete(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context = {'request': request})
        return Response(serializer.data)

    def put(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
