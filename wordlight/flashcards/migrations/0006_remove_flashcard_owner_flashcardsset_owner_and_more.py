# Generated by Django 5.0.6 on 2024-10-11 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flashcards", "0005_flashcardsset_language_variation"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="flashcard",
            name="owner",
        ),
        migrations.AddField(
            model_name="flashcardsset",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="owned_flashcards",
                to="users.profile",
            ),
        ),
        migrations.AlterField(
            model_name="flashcard",
            name="set",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="flashcards.flashcardsset",
            ),
        ),
    ]
