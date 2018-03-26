# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class ProfileEntry(models.Model):
    last_name     = models.CharField(max_length=20, blank=True, null=True)
    first_name    = models.CharField(max_length=20, blank=True, null=True)
    username      = models.CharField(max_length=20)
    bio           = models.CharField(max_length=20, blank=True, null=True)
    update_time   = models.DateTimeField(blank=True, null=True)
    user          = models.ForeignKey(User)

    def __unicode__(self):
        return 'ProfileEntry(id=' + str(self.username) + ')'

class Follower(models.Model):
    last_name     = models.CharField(max_length=20, blank=True, null=True)
    first_name    = models.CharField(max_length=20, blank=True, null=True)
    username      = models.CharField(max_length=20, blank=True, null=True)
    followers     = models.ManyToManyField(ProfileEntry)

    def __unicode__(self):
        return 'FollowerEntry(id=' + str(self.username) + ')'

class Album(models.Model):
    user          = models.ForeignKey(User)
    name          = models.CharField(max_length=50, blank=True, null=True)
    description   = models.CharField(max_length=200, blank=True, null=True)
    picture       = models.FileField(upload_to="images", blank=True, null=True)
    profilio      = models.ManyToManyField(ProfileEntry)
    update_time   = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return 'album(id=' + str(self.id) + ')'

class Song(models.Model):
    user          = models.ForeignKey(User)
    name          = models.CharField(max_length=50, blank=True, null=True)
    description   = models.CharField(max_length=200, blank=True, null=True)
    picture       = models.FileField(upload_to="images", blank=True, null=True)
    update_time   = models.DateTimeField(blank=True, null=True)
    album         = models.ManyToManyField(Album)

    def __unicode__(self):
        return 'song(id=' + str(self.id) + ')'

class Workspace(models.Model):
    user          = models.ForeignKey(User)
    song          = models.ManyToManyField(Song)
    update_time   = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return 'workspace(id=' + str(self.id) + ')'

class Track(models.Model):
    user          = models.ForeignKey(User)
    workspace     = models.ManyToManyField(Workspace)
    update_time   = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return 'track(id=' + str(self.id) + ')'
