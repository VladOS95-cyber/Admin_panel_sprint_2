from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from movies.models import Filmwork


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ["get"]

    def get_queryset(self):
        return Filmwork.objects.prefetch_related("film_genres", "persons").annotate(
            actors=ArrayAgg(
                "persons__full_name",
                distinct=True,
                filter=Q(personfilmwork__role="actor"),
            ),
            genres=ArrayAgg("film_genres__name", distinct=True),
            directors=ArrayAgg(
                "persons__full_name",
                distinct=True,
                filter=Q(personfilmwork__role="director"),
            ),
            writers=ArrayAgg(
                "persons__full_name",
                distinct=True,
                filter=Q(personfilmwork__role="writer"),
            ),
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class Movies(MoviesApiMixin, BaseListView):
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        input_queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            input_queryset, self.paginate_by
        )
        values = queryset.values(
            "id",
            "title",
            "description",
            "creation_date",
            "rating",
            "type",
            "genres",
            "actors",
            "directors",
            "writers",
        )

        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "prev": page.previous_page_number() if page.has_previous() else None,
            "next": page.next_page_number() if page.has_next() else None,
            "results": list(values),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    def get_context_data(self, **kwargs):
        film = kwargs["object"]
        context = {
            "id": film.id,
            "title": film.title,
            "description": film.description,
            "creation_date": film.creation_date,
            "rating": film.rating,
            "type": film.type,
            "genres": film.genres,
            "actors": film.actors,
            "directors": film.directors,
            "writers": film.writers,
        }
        return context
