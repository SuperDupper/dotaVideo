from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User, Group
from dotavideo.models import Video, VideoAuthor
from rest_framework import viewsets, routers

#admin.autodiscover()


class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

class VideoAuthorViewSet(viewsets.ModelViewSet):
    model = VideoAuthor

class VideoViewSet(viewsets.ModelViewSet):
    model = Video


# routers provides an easy way of automatically determine the url conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'videoauthors', VideoAuthorViewSet)
router.register(r'videos', VideoViewSet) 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^author/list/$', list_author),
    #url(r'^author/(?P<author>[^/])/list/$', list_author_video),
)
