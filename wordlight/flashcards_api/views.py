from django.shortcuts import render
from rest_framework.viewsets import generics
from flashcards_api.serializers import FlashcardSerializer
from flashcards.models import Flashcard


class GetAllFlashcardsForUser(generics.ListAPIView):
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        return Flashcard.objects.filter(owner=self.request.user.profile)


class GetAllFlashcardsForSet(generics.ListAPIView):
    serializer_class = FlashcardSerializer

    def get_queryset(self, *args, **kwargs):
        return Flashcard.objects.filter(
            owner=self.request.user.profile, set__set_name=self.kwargs["set_name"]
        )
