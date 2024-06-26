from django.forms import ModelForm
from application.models import application

class application_form(ModelForm):
    class Meta():
        model = application
        fields = ['name', 'email', 'age','expect_salary','resume_url']

