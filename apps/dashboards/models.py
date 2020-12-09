from django.db import models
from apps.utils.models import Timestamp
from apps.accounts.models import User


class Dashboard(Timestamp, models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    message = models.TextField()
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
