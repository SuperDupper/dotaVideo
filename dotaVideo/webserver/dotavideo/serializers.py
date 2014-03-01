from django.forms import widgets
from rest_framework import serializers
from dotavideo.models import Video, VideoAuthor

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Author
    fields = ('nick', 'url', 'video_type')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Video
    fields = ('url', 'title', 'abstract', 'author', 'release_time', 'watch_num', 'video_length', 'video_type')
