from django.db import models
from users.models import Profile


class LanguagesVariations(models.TextChoices):
    POL_TO_ENG = ("1", "Polish --> English")
    ENG_TO_POL = ("2", "English --> Polish")
    POL_TO_GE = ("3", "Polish --> German")


class FlashcardsSet(models.Model):
    set_name = models.CharField(max_length=255)
    language_variation = models.CharField(
        choices=LanguagesVariations, default=LanguagesVariations.POL_TO_ENG
    )

    def __str__(self):
        return self.set_name


class Flashcard(models.Model):
    original_text = models.CharField(max_length=255)
    translated_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        to=Profile,
        related_name="owned_flashcards",
        null=True,
        on_delete=models.SET_NULL,
    )
    invited_users = models.ManyToManyField(
        to=Profile, related_name="shared_flashcards", null=True, blank=True
    )
    set = models.ForeignKey(to=FlashcardsSet, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.original_text
