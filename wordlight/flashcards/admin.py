from django.contrib import admin
from flashcards.models import Flashcard, FlashcardsSet, Points

admin.site.register((Flashcard, FlashcardsSet, Points))
