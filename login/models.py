from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    character = models.CharField(max_length=10, blank=True)

    class Meta(AbstractUser.Meta):
        pass
