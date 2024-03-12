from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Events(models.Model):
    class Meta:
        verbose_name_plural = "Eventos"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)
    public = models.BooleanField(default=False, null=True, blank=True)
    allDay = models.BooleanField(default=False, null=True, blank=True)
