from rest_framework import generics
from snacks_project.permissions import IsOwnerOrReadOnly

from .models import Snack, SnackCollection
from .serializer import SnackSerializer, SnackCollectionSerializer


class SnackListCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackCollectionListCreate(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = SnackCollection.objects.all()
    serializer_class = SnackCollectionSerializer


class SnackCollectionUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = SnackCollection.objects.all()
    serializer_class = SnackCollectionSerializer
