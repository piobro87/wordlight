from users.views import RegisterView, CustomLoginView
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
]
