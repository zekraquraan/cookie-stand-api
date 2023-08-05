from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import book


class bookListView(LoginRequiredMixin, ListView):
    template_name = "books/book_list.html"
    model = book
    context_object_name = "books"


class bookDetailView(LoginRequiredMixin, DetailView):
    template_name = "books/book_detail.html"
    model = book


class bookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "books/book_update.html"
    model = book
    fields = "__all__"


class bookCreateView(LoginRequiredMixin, CreateView):
    template_name = "books/book_create.html"
    model = book
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class bookDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "books/book_delete.html"
    model = book
    success_url = reverse_lazy("book_list")
