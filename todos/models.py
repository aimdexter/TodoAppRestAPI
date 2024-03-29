from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
