from django.db import models
from django.urls import reverse
class Project(models.Model):
    name = models.CharField(max_length=100)
    hardware = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'project_id': self.id})
