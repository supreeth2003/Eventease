from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(default=now)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="event_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # TEMPORARILY ALLOW NULL
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 

    def __str__(self):
        return self.name



