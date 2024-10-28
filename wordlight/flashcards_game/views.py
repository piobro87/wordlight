from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class FlashcardsPlay(TemplateView):
    template_name = "flashcards_game/flashcards_game.html"
