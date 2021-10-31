# Generated by Django 3.2 on 2021-10-19 11:19

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Filmwork",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                (
                    "creation_date",
                    models.DateField(blank=True, verbose_name="creation date"),
                ),
                (
                    "certificate",
                    models.TextField(blank=True, verbose_name="certificate"),
                ),
                (
                    "file_path",
                    models.FileField(
                        blank=True, upload_to="film_works/", verbose_name="file"
                    ),
                ),
                (
                    "rating",
                    models.FloatField(
                        blank=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(10.0),
                        ],
                        verbose_name="rating",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("movie", "movie"), ("tv_show", "TV Show")],
                        max_length=20,
                        verbose_name="type",
                    ),
                ),
            ],
            options={
                "verbose_name": "filmwork",
                "verbose_name_plural": "filmworks",
                "db_table": "film_work",
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="title")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "genre",
                "verbose_name_plural": "genres",
                "db_table": "genre",
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=255, verbose_name="full_name"),
                ),
                ("birth_date", models.DateField(blank=True, verbose_name="birth_date")),
            ],
            options={
                "verbose_name": "person",
                "verbose_name_plural": "persons",
                "db_table": "person",
            },
        ),
        migrations.CreateModel(
            name="PersonFilmWork",
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
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("director", "director"),
                            ("writer", "writer"),
                            ("actor", "actor"),
                        ],
                        max_length=20,
                        verbose_name="role",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                        verbose_name="film_work",
                    ),
                ),
                (
                    "person",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.person",
                        verbose_name="person",
                    ),
                ),
            ],
            options={
                "db_table": "person_film_work",
                "unique_together": {("film_work", "person", "role")},
            },
        ),
        migrations.CreateModel(
            name="FilmworkGenre",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "film_work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movies.filmwork",
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="movies.genre"
                    ),
                ),
            ],
            options={
                "db_table": "genre_film_work",
                "unique_together": {("film_work", "genre")},
            },
        ),
        migrations.AddField(
            model_name="filmwork",
            name="genres",
            field=models.ManyToManyField(
                through="movies.FilmworkGenre", to="movies.Genre"
            ),
        ),
        migrations.AddField(
            model_name="filmwork",
            name="persons",
            field=models.ManyToManyField(
                through="movies.PersonFilmWork", to="movies.Person"
            ),
        ),
    ]
