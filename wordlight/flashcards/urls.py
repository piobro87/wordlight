from core.views import HomeView
from django.urls import path

from flashcards.views import FlashcardsPreview

from flashcards_api.views import GetAllFlashcardsForSet

urlpatterns = [path("flashcards/", FlashcardsPreview.as_view(), name="flashcards")]
