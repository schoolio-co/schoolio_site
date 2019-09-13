from django.db import models
from schoolio.models import school

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=30, default='main')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    school = models.ForeignKey(school, 
							on_delete=models.CASCADE,
							blank=True,
        					null=True)

    def __str__(self):
        return self.title