from core.views import HomeView
from django.urls import path

from flashcards.views import AllFlashcardsSetsPreview

from flashcards.views import FlashcardsByCategoryPreview

urlpatterns = [
    path("flashcards/", AllFlashcardsSetsPreview.as_view(), name="flashcards"),
    path(
        "flashcards/<slug:category>/",
        FlashcardsByCategoryPreview.as_view(),
        name="flashcards_category",
    ),
]
