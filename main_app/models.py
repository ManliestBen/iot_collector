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

class Progress(models.Model):
    date = models.DateField('progress date')
    note = models.CharField(max_length=100)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.note} on {self.date}"
    class Meta:
        ordering = ['-date']