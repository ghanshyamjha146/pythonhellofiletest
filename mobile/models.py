from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length = 25, blank = True, null = True)
    phone = models.CharField(max_length = 20, blank = False, null = False)

    class Meta:
        db_table = 'user'





