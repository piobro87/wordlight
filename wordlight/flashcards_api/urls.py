from django.urls import path
from flashcards_api.views import GetAllFlashcardsForUser
from flashcards_api.views import GetDeleteFlashcardsForCategory
from flashcards_api.views import CreateFlashcardForCategory
from flashcards_api.views import DeleteFlashcard
from flashcards_api.views import CreateNewCategory
from flashcards_api.views import CheckAnswers

urlpatterns = [
    path("flashcards/", GetAllFlashcardsForUser.as_view(), name="get_flashcards"),
    path(
        "flashcards/<slug:category>/",
        GetDeleteFlashcardsForCategory.as_view(),
        name="flashcards_by_category",
    ),
    path("flashcard/", CreateFlashcardForCategory.as_view(), name="create_flashcard"),
    path("flashcard/<slug:id>", DeleteFlashcard.as_view(), name="delete_flashcard"),
    path("flashcard-set/", CreateNewCategory.as_view(), name="create_category"),
    path("flashcard-check/", CheckAnswers.as_view(), name="check_answers"),
]
