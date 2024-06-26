from django.contrib import admin
from django.urls import path
from job import views

urlpatterns = [
    path('job_creation/', views.job_creation,name='job_creation'),
    path('job_list/', views.job_list,name='job_list'),
    path('jobseeker_list/', views.jobseeker_list,name='jobseeker_list'),
    
    path('job_details/<int:id>', views.job_details,name='job_details'),
    path('job_delete/<int:id>', views.job_delete,name='job_delete'),
    path('applications', views.applications,name='applications'),
]
