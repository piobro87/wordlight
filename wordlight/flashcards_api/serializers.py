from rest_framework import serializers
from flashcards.models import Flashcard, FlashcardsSet


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = "__all__"


class CreateFlashcardSerializer(serializers.ModelSerializer):
    set_name = serializers.CharField(write_only=True)

    class Meta:
        model = Flashcard
        fields = ["original_text", "translated_text", "set_name"]

    def create(self, validated_data):
        print(validated_data, flush=True)

        # Retrieve the set name from the validated data
        set_name = validated_data.pop("set_name")

        try:
            flashcard_set = FlashcardsSet.objects.get(set_name=set_name)
        except FlashcardsSet.DoesNotExist:
            raise serializers.ValidationError(
                {"set_name": "Set with this name does not exist."}
            )
        # Add the owner field from the request user to the validated data
        validated_data["owner"] = self.context["request"].user.profile
        validated_data["set"] = flashcard_set

        return super().create(validated_data)
