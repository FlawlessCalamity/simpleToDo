from django.db import models

# Create your models here.


class ToDoList(models.Model):
    task = models.TextField(blank=False)
    completed = models.BooleanField(default=False)
