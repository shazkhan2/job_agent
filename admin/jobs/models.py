from django.db import models

# Create your models here.
class JobListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=50)
    job_url = models.URLField(max_length=500, unique=True)
    
    def __str__(self):
        return f"{self.title} ({self.source})"