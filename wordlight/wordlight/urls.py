from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import core.urls as core_urls
import users.urls as users_urls
import flashcards.urls as flashcards_urls
import flashcards_api.urls as flashcards_api_urls
import flashcards_game.urls as flashcards_game_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(core_urls)),
    path("", include(users_urls)),
    path("", include(flashcards_urls)),
    path("api/", include(flashcards_api_urls)),
    path("game/", include(flashcards_game_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
