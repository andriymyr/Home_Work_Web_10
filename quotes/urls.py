from django.urls import path
from . import views

app_name = "quotes"
urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("/authors", views.authors, name="authors"),
    path("/add_author", views.add_author, name="add_author"),
    path("/add_quote", views.add_quotes, name="add_quote"),
    path(
        "author_description/<str:author_name>/",
        views.author_description,
        name="author_description",
    ),
]
