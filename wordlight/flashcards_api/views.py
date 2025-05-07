from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from flashcards.models import Flashcard, Points
from flashcards.models import FlashcardsSet
from flashcards_api.exceptions import CardNotFound
from flashcards_api.exceptions import CategoryAlreadyExists
from flashcards_api.helpers import share_flashcard_set
from flashcards_api.serializers import CreateFlashcardSerializer
from flashcards_api.serializers import CreateNewCategorySerializer
from flashcards_api.serializers import FlashcardSerializer
from rest_framework import views, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import generics


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
        )

        cards.delete()

        return JsonResponse(data={}, status=204)


class CreateFlashcardForCategory(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateFlashcardSerializer


class DeleteFlashcard(LoginRequiredMixin, generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        card = Flashcard.objects.filter(
            set__owner=self.request.user.profile, id=self.kwargs["id"]
        )

        if card is None:
            raise CardNotFound()

        card.delete()
        return JsonResponse(data={}, status=204)


class CreateNewCategory(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = CreateNewCategorySerializer

    def perform_create(self, serializer):
        category_name = serializer.validated_data.get("set_name").lower()
        owner = self.request.user.profile
        if FlashcardsSet.objects.filter(set_name=category_name, owner=owner).exists():
            raise CategoryAlreadyExists()

        serializer.save()


class CheckAnswers(LoginRequiredMixin, views.APIView):
    def post(self, request):
        """
        Expected format:
        {
            "category": ...,
            "answers": [
                {
                "id": <input_id>,
                "answer": <input_value>
                },
                {...}
            ]
        }
        """
        results = {}
        details = request.data
        answers = details["answers"]
        category = details["category"]

        for answer in answers:
            id = answer.get("id")
            value = answer.get("answer")

            card = Flashcard.objects.get(id=id)
            is_correct = card.translated_text == value
            results[id] = is_correct

        positive_points = len(
            list(filter(lambda pair: pair[1] is True, results.items()))
        )
        total_answers = len(answers)

        category_obj = FlashcardsSet.objects.get(set_name=category)
        Points.objects.create(
            flashcards_set=category_obj,
            positive_answers=positive_points,
            total_answers=total_answers,
        )

        return JsonResponse(results)


class ShareCategoryView(LoginRequiredMixin, views.APIView):
    def post(self, request):
        sharer_id = request.data.get("sharer")
        recipient_email = request.data.get("recipient")
        category_id = request.data.get("category_id")

        new_flashcard_set = share_flashcard_set(sharer_id, recipient_email, category_id)

        return Response(
            {
                "message": "Flashcard set successfully shared.",
                "new_set_id": new_flashcard_set.id,
            },
            status=status.HTTP_201_CREATED,
        )


class DeleteCategory(LoginRequiredMixin, generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        category_name = self.kwargs["set_name"]
        category = get_object_or_404(
            FlashcardsSet, owner=self.request.user.profile, set_name=category_name
        )
        category.delete()
        return JsonResponse(data={}, status=204)
