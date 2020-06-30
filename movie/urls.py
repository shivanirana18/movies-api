from django.conf.urls import url
from movie import views

urlpatterns= [
    url(r'movies/?$', views.MovieListCreate.as_view()),
    url(r'movies/(?P<primaryid>[0-9]+)$', views.MovieRetrieveUpdateDestroy.as_view()),
]