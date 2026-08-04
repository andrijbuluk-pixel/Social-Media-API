from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
    ("R", "Rather not say"),
    )

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username} - {self.email}"
