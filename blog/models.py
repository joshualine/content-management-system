from django.db import models
from slugger import AutoSlugField
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):

    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
