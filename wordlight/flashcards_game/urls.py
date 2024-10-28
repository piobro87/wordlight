from django.urls import path

from flashcards_game.views import FlashcardsPlay

urlpatterns = [
    path("<slug:category>/play", FlashcardsPlay.as_view(), name="flashcards_play"),
]
