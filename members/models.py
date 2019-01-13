from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.username
