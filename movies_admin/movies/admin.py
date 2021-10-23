from django.contrib import admin

from .models import Filmwork, FilmworkGenre, Genre, Person, PersonFilmWork


class PersonRoleInline(admin.TabularInline):
    model = PersonFilmWork
    extra = 0


class GenresInline(admin.TabularInline):
    model = FilmworkGenre
    extra = 0


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "creation_date", "rating")
    list_filter = ("type", "genres", "persons")
    fields = (
        "title",
        "type",
        "description",
        "creation_date",
        "certificate",
        "file_path",
        "rating",
    )
    inlines = [PersonRoleInline, GenresInline]


@admin.register(Person)
class Personadmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_date")
    list_filter = ("birth_date",)
    fields = ("full_name", "birth_date")


@admin.register(Genre)
class Genreadmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    fields = ("name", "description")
