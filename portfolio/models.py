from django.db import models
from django.utils.text import slugify
import json


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Enter Bootstrap Icon class name (e.g., 'bi bi-laptop')")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
           if not self.slug:
               self.slug = slugify(self.title)
           super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    project_url = models.URLField(blank=True, null=True)
    technology = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
           if not self.slug:
               self.slug = slugify(self.title)  # Automatically create a slug from the title
           super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

