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

        set_name = validated_data.pop("set_name")
        owner = self.context["request"].user.profile

        try:
            flashcard_set = FlashcardsSet.objects.filter(
                set_name=set_name, owner=owner
            ).first()
        except FlashcardsSet.DoesNotExist:
            raise serializers.ValidationError(
                {"set_name": "Set with this name does not exist."}
            )

        validated_data["set"] = flashcard_set

        return super().create(validated_data)


class CreateNewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardsSet
        fields = "__all__"

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user.profile

        return super().create(validated_data)
