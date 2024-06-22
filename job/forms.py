from django import forms
from job.models import job_model

class job_model_form(forms.ModelForm):
    class Meta:
        model=job_model
        fields="__all__"