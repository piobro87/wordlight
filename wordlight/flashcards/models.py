from django.db import models
from users.models import Profile


class FlashcardsSet(models.Model):
    set_name = models.CharField(max_length=255)


class Flashcard(models.Model):
    original_text = models.CharField(max_length=255)
    translated_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(to=Profile)
    set = models.ForeignKey(to=FlashcardsSet, null=True, on_delete=models.SET_NULL)
