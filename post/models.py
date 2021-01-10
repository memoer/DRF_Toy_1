from django.contrib.auth.models import User
from django.db import models
from core.models import Common


class Subject(models.Model):
    name = models.CharField(max_length=64)


class Post(Common):
    GAME = "GAME"
    DAILY = "DAILY"
    BOOK = "BOOK"
    DEV = "DEV"
    FOOD = "FOOD"
    CATEGORY_CHOICES = [
        (GAME, "Game"),
        (DAILY, "Daily"),
        (BOOK, "Book"),
        (DEV, "Dev"),
        (FOOD, "Food"),
    ]
    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ManyToManyField(
        Subject, related_name="post", null=True, blank=True
    )

    def __str__(self):
        return self.title


class Photo(models.Model):
    location = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)