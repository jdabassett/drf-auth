from django.urls import path

from .views import SnackListCreate, SnackUpdate, SnackCollectionListCreate, SnackCollectionUpdate

urlpatterns = [
    path("create/",SnackListCreate.as_view(), name="snack_create"),
    path("create/<int:pk>", SnackUpdate.as_view(), name="snack_update"),
    path("collection/create/", SnackCollectionListCreate.as_view(), name="collection_create"),
    path("collection/create/<int:pk>", SnackCollectionUpdate.as_view(), name="collection_update"),
]
