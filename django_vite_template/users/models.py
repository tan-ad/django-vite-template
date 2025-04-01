from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add custom fields here later if needed
    # For example:
    # date_of_birth = models.DateField(null=True, blank=True)
    pass # Keep 'pass' if you have no custom fields yet

    def __str__(self):
        return self.username
