from django.db import models
from job.models import job_model

# Create your models here.

class application(models.Model):
    PROGRESS_CHOICE=[
         ('applied', 'Applied'),
         ('shortlisted', 'Shortlisted'),
         ('selected', 'Selected'),
    ]
    job=models.ForeignKey(job_model, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    age=models.IntegerField()
    expect_salary=models.IntegerField()
    resume_url=models.URLField(max_length=250)
    progress = models.CharField(max_length=20, choices=PROGRESS_CHOICE, default='applied')
    apply_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name