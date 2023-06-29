from django.db import models


class Message(models.Model):
    to = models.EmailField()
    subject = models.CharField(max_length=64)
    message = models.TextField()
