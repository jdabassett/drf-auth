
from django.contrib import admin
from .models import Snack, SnackCollection


class SnackAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "description",
    )


class SnackCollectionAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
    )


admin.site.register(Snack, SnackAdmin)
admin.site.register(SnackCollection, SnackCollectionAdmin)
