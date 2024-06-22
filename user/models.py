# registration/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField(default=False)
    is_job_seeker = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
