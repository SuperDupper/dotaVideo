from django.shortcuts import render
from rest_framework import viewsets
from dotavideo.serializers import AuthorSerializer, VideoSerializer
from dotavideo.models import Video, VideoAuthor


class AuthorViewSet(viewsets.ModelViewSet):
  queryset = VideoAuthor.objects.all()
  serializer_class = AuthorSerializer

class VideoViewSet(viewsets.ModelViewSet):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

# Create your views here.
