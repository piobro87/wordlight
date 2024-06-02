# Generated by Django 5.0.4 on 2024-06-02 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FlashcardsSet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("set_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Flashcard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_text", models.CharField(max_length=255)),
                ("translated_text", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("users", models.ManyToManyField(to="users.profile")),
                (
                    "set",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="flashcards.flashcardsset",
                    ),
                ),
            ],
        ),
    ]
