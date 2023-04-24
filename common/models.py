from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    PRIORITY_CHOICES = (
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    )
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    published_at = models.DateTimeField(auto_now_add=True)
