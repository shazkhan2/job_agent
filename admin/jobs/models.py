from django.db import models
from django.utils import timezone

# Create your models here.
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50)
    job_url = models.URLField(max_length=500, unique=True)
    
    def __str__(self):
        return f"{self.title} ({self.source})"
    
class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    posted_date = models.DateField(default=timezone.now)
    job_url = models.URLField(max_length=500, unique=True)
    source = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.title} at {self.company} ({self.source})"
    class Meta:
        ordering = ['-posted_date']