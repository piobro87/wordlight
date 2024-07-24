"""
URL configuration for wordlight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import core.urls as core_urls
import users.urls as users_urls
import flashcards.urls as flashcards_urls
import flashcards_api.urls as flashcards_api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(core_urls)),
    path("", include(users_urls)),
    path("", include(flashcards_urls)),
    path("api/", include(flashcards_api_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
