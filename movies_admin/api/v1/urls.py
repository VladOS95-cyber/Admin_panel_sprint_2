from django.urls import path

from api.v1 import views


urlpatterns = [path("movies/", views.Movies.as_view())]
