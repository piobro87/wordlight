from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from flashcards.models import FlashcardsSet, Flashcard, Points
from collections import defaultdict


class AllFlashcardsSetsPreview(LoginRequiredMixin, ListView):
    template_name = "flashcards/flashcards_sets.html"
    model = FlashcardsSet
    context_object_name = "sets"

    def get_queryset(self):
        sets = FlashcardsSet.objects.filter(owner=self.request.user.profile)

        return sets


class FlashcardsByCategoryPreview(LoginRequiredMixin, TemplateView):
    template_name = "flashcards/flashcards.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        category_name = self.kwargs["category"]
        _ = get_object_or_404(FlashcardsSet, set_name=category_name)

        context["category"] = self.kwargs["category"]

        return context


class FlashcardsStatisticsPreview(LoginRequiredMixin, ListView):
    template_name = "flashcards/statistics.html"
    context_object_name = "points"

    def get_queryset(self):
        queryset = Points.objects.values(
            "flashcards_set__set_name",
            "created_at",
            "total_answers",
            "positive_answers",
        ).order_by(
            "flashcards_set__set_name", "created_at"
        )  # Order results for better grouping

        grouped_data = defaultdict(list)
        for item in queryset:
            grouped_data[item["flashcards_set__set_name"]].append(
                {
                    "created_at": item["created_at"],
                    "total_answers": item["total_answers"],
                    "positive_answers": item["positive_answers"],
                }
            )

        return dict(grouped_data)  # Convert defaultdict to a normal dictionary
