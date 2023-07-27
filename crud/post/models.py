from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    content = models.TextField(max_length=255, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post:list_post_view', kwargs={})
