# hackathon/models.py

from django.db import models
import uuid
from django.utils import timezone

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    team_members = models.TextField()
    email = models.EmailField(default="vedantsomani210474@acropolis.in")
    access_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    api_code = models.CharField(max_length=255, null=True, blank=True)  # Add this field to store the api_code



class ApiHitCount(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    api_code = models.CharField(max_length=255)  # Change to CharField to store custom format
    time_refreshed = models.DateTimeField(default=timezone.now)
    api_hits = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)