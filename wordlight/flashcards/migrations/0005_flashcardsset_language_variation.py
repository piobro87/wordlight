# Generated by Django 5.0.6 on 2024-07-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0004_alter_flashcard_invited_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="flashcardsset",
            name="language_variation",
            field=models.CharField(
                choices=[
                    ("1", "Polish --> English"),
                    ("2", "English --> Polish"),
                    ("3", "Polish --> German"),
                ],
                default="1",
            ),
        ),
    ]