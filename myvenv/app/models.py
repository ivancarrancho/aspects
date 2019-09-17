from django.db import models
from django.utils import timezone


class Aspects(models.Model):
    title = models.CharField(max_length=200)
    history_type = models.TextField()
    user = models.CharField(max_length=200)
    description = models.TextField()
    criteria_of_acceptance = models.TextField()
    interface_requirements = models.TextField()
    dependencies = models.TextField()

    def __str__(self):
        return self.title