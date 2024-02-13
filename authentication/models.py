from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models

from authentication.utils import generate_unique_id
from orders.models import Category


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
    unique_id = models.CharField(max_length=256, default=generate_unique_id)
    email = models.CharField(blank=True, null=True, max_length=512)

    is_staff = models.BooleanField(default=False)

    liked_category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь API"
        verbose_name_plural = "Пользователи API"
        constraints = [
            models.UniqueConstraint(fields=["unique_id"], name="unique_username"),
        ]

    def __str__(self):
        return self.username
