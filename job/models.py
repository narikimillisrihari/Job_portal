from django.db import models
from user.models import Profile

# Create your models here.
class job_model(models.Model):
    job_title=models.CharField(max_length=200)
    job_location = models.CharField(max_length=100)
    job_description=models.TextField()
    job_posted_date = models.DateTimeField(auto_now_add=True)
    apply_url=models.URLField()
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='jobs_posted')

    def __str__(self):
        return self.job_title