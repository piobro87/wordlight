from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from flashcards.models import FlashcardsSet, Flashcard


class AllFlashcardsSetsPreview(LoginRequiredMixin, ListView):
    template_name = "flashcards/flashcards_sets.html"
    model = FlashcardsSet
    context_object_name = "sets"

    def get_queryset(self):
        sets = FlashcardsSet.objects.filter(owner=self.request.user.profile)
        print("XXX", sets, flush=True)

        return sets


class FlashcardsByCategoryPreview(LoginRequiredMixin, TemplateView):
    template_name = "flashcards/flashcards.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        category_name = self.kwargs["category"]
        _ = get_object_or_404(FlashcardsSet, set_name=category_name)

        context["category"] = self.kwargs["category"]

        return context
