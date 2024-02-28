from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import UserRegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("login")
    success_message = f"Account's been created!"
