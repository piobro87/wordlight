from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class FlashcardsPreview(LoginRequiredMixin, TemplateView):
    template_name = "flashcards/flashcards.html"
