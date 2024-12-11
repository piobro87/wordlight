import json

from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.viewsets import generics
from flashcards_api.serializers import FlashcardSerializer
from flashcards.models import Flashcard

from flashcards_api.serializers import CreateFlashcardSerializer

from flashcards_api.serializers import CreateNewCategorySerializer
from rest_framework import views
from flashcards.models import Flashcard

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class GetAllFlashcardsForUser(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        return Flashcard.objects.filter(set__owner=self.request.user.profile)


class GetDeleteFlashcardsForCategory(
    LoginRequiredMixin, generics.ListAPIView, generics.DestroyAPIView
):
    serializer_class = FlashcardSerializer

    def get_queryset(self, *args, **kwargs):
        return Flashcard.objects.filter(
            set__owner=self.request.user.profile, set__set_name=self.kwargs["category"]
        )

    def delete(self, request, *args, **kwargs):
        cards = Flashcard.objects.filter(
            set__owner=self.request.user.profile, set__set_name=self.kwargs["category"]
        ).delete()

        return JsonResponse(data={}, status=204)


class CreateFlashcardForCategory(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateFlashcardSerializer


class DeleteFlashcard(LoginRequiredMixin, generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        card = Flashcard.objects.filter(
            set__owner=self.request.user.profile, id=self.kwargs["id"]
        )

        if card is None:
            raise Http404()

        card.delete()
        return JsonResponse(data={}, status=204)


class CreateNewCategory(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateNewCategorySerializer


class CheckAnswers(LoginRequiredMixin, views.APIView):
    def post(self, request, *args, **kwargs):
        """
        Expected format:
        [
            {
                "id": <input_id>,
                "answer": <input_value>
            },
            {...}
        ]
        """
        results = {}
        answers = request.data

        for answer in answers:
            id = answer.get("id")
            value = answer.get("answer")

            card = Flashcard.objects.get(id=id)
            is_correct = card.translated_text == value
            results[id] = is_correct

        return JsonResponse(results)
