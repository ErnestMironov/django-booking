from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user with email as login and role field."""

    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=[("user", "user"), ("admin", "admin")],
        default="user",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS (it's USERNAME_FIELD)

    def __str__(self):
        return self.email
