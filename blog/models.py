from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # The timezone.now is a function with () but without the braces wont execute
    date_posted = models.DateTimeField(default=timezone.now)
    # If a user is deleted, delete the posts as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
