from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import book
from .permissions import IsOwnerOrReadOnly
from .serializers import bookSerializer


class bookList(ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class = bookSerializer


class bookDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = book.objects.all()
    serializer_class = bookSerializer
