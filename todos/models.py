from django.db import models
from authentication.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)


class Board(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class List(models.Model):
    title = models.CharField(max_length=255)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    ord = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Card(models.Model):
    title = models.CharField(max_length=255)
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    ord = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(models.Model):
    title = models.CharField(max_length=255)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BoardMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["user", "board"]


class CardAssignment(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["card", "user"]
