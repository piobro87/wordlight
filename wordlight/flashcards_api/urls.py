from django.urls import path

from flashcards_api.views import GetAllFlashcardsForUser

from flashcards_api.views import GetAllFlashcardsForSet

urlpatterns = [
    path("flashcards/", GetAllFlashcardsForUser.as_view(), name="get_flashcards"),
    path(
        "flashcards/<slug:set_name>/",
        GetAllFlashcardsForSet.as_view(),
        name="flashcards_by_set",
    ),
]
