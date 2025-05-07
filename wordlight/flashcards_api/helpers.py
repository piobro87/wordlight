from flashcards.models import FlashcardsSet, Flashcard
from rest_framework.generics import get_object_or_404
from users.models import Profile


def share_flashcard_set(
    sharer_id: int, recipient_email: str, category_name: str
) -> FlashcardsSet:
    sharer = get_object_or_404(Profile, id=int(sharer_id))
    recipient = get_object_or_404(Profile, user__email=recipient_email)
    flashcard_set = get_object_or_404(
        FlashcardsSet, set_name=category_name, owner=sharer
    )

    new_flashcard_set = FlashcardsSet.objects.create(
        set_name=f"{flashcard_set.set_name}-shared",
        language_variation=flashcard_set.language_variation,
        owner=recipient,
    )

    flashcards = Flashcard.objects.filter(set=flashcard_set)
    for flashcard in flashcards:
        Flashcard.objects.create(
            original_text=flashcard.original_text,
            translated_text=flashcard.translated_text,
            set=new_flashcard_set,
        )

    return new_flashcard_set
