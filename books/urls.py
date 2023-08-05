from django.urls import path
from .views import bookList, bookDetail

urlpatterns = [
    path("", bookList.as_view(), name="book_list"),
    path("<int:pk>/", bookDetail.as_view(), name="book_detail"),
]
