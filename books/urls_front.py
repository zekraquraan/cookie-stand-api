from django.urls import path
from .views_front import (
    bookCreateView,
    bookDeleteView,
    bookDetailView,
    bookListView,
    bookUpdateView,
)

urlpatterns = [
    path("", bookListView.as_view(), name="book_list"),
    path("<int:pk>/", bookDetailView.as_view(), name="book_detail"),
    path("create/", bookCreateView.as_view(), name="book_create"),
    path("<int:pk>/update/", bookUpdateView.as_view(), name="book_update"),
    path("<int:pk>/delete/", bookDeleteView.as_view(), name="book_delete"),
]
