from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoModel(models.Model):
    title = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title