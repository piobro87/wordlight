# Generated by Django 5.0.6 on 2024-07-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0002_remove_flashcard_users_flashcard_invited_users_and_more"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flashcard",
            name="invited_users",
            field=models.ManyToManyField(
                null=True, related_name="shared_flashcards", to="users.profile"
            ),
        ),
    ]
