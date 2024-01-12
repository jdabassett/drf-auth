# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
        blank=True,
    )

    def __str__(self):
        return self.username