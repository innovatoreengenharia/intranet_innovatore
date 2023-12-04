from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    class Meta:
        verbose_name_plural = "Eventos"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    public = models.BooleanField(default=False, null=True, blank=True)
    allDay = models.BooleanField(default=False, null=True, blank=True)
