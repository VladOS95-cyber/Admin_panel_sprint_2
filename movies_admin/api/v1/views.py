from django.http import JsonResponse
from django.views import View
from django.contrib.postgres.aggregates import ArrayAgg
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from movies.models import Filmwork


class Movies(BaseListView):
    model = Filmwork
    http_method_names = ["get"]
    paginate_by = 50

    def get_queryset(self):
        return (
            Filmwork.objects.prefetch_related("genres", "persons")
            .annotate(
                persons_arr=ArrayAgg("persons__full_name", distinct=True),
                genres_arr=ArrayAgg("genres__name", distinct=True),
            )
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by)

        context = {
            "count": paginator.count,
            "total_pages": paginator.num_pages,
            "results": list(
                queryset.values("title", "persons_arr", "genres_arr")),
            "prev": paginator.page(2).previous_page_number(),
            "next": paginator.page(1).next_page_number()
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(View):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        # Получение и обработка данных
        return JsonResponse({})
