from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.viewsets import generics
from flashcards_api.serializers import FlashcardSerializer
from flashcards.models import Flashcard

from flashcards_api.serializers import CreateFlashcardSerializer


class GetAllFlashcardsForUser(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        return Flashcard.objects.filter(owner=self.request.user.profile)


class GetDeleteFlashcardsForCategory(
    LoginRequiredMixin, generics.ListAPIView, generics.DestroyAPIView
):
    serializer_class = FlashcardSerializer

    def get_queryset(self, *args, **kwargs):
        return Flashcard.objects.filter(
            owner=self.request.user.profile, set__set_name=self.kwargs["category"]
        )

    def delete(self, request, *args, **kwargs):
        cards = Flashcard.objects.filter(
            owner=self.request.user.profile, set__set_name=self.kwargs["category"]
        ).delete()

        return JsonResponse(data={}, status=204)


class CreateFlashcardForCategory(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateFlashcardSerializer


class DeleteFlashcard(LoginRequiredMixin, generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        card = Flashcard.objects.filter(
            owner=self.request.user.profile, id=self.kwargs["id"]
        )

        if card is None:
            raise Http404()

        card.delete()
        return JsonResponse(data={}, status=204)


# class DeleteFlashcardsForCategory(LoginRequiredMixin, generics.DestroyAPIView):
#     def delete(self, request, *args, **kwargs):
#         cards = Flashcard.objects.filter(owner=self.request.user.profile, set__set_name=self.kwargs[
#             "category"]).delete()
#
#         return JsonResponse(data={}, status=204)
