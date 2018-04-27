from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from magicmusic import views
# from community import views as comm_views

from magicmusic import views

urlpatterns = [
    url(r'^$', views.mymusic, name='mymusic'),
    # url(r'^profile(?P<user_id>\d+)$', comm_views.profile, name='profile'),
    # url(r'^follower', views.follower, name='follower'),
    url(r'^addworkspace', views.addworkspace, name='addworkspace'),
    url(r'^workspace/(?P<id>\d+)$', views.workspace, name='workspace'),
    url(r'^track/(?P<id>\d+)$', views.track, name='track'),
    url(r'^generate-music/(?P<trackID>\d+)$', views.generate_music, name='generate-music'),
    url(r'^generate-workspace-music/(?P<workspace_id>\d+)$', views.generate_workspace_music,
        name='generate-workspace-music'),
]