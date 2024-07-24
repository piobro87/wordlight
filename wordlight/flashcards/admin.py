from django.contrib import admin
from flashcards.models import Flashcard, FlashcardsSet

admin.site.register((Flashcard, FlashcardsSet))
