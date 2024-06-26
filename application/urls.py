from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('apply/<int:id>', views.apply,name='apply'),
    path('status/', views.status,name='status'),
     path('update_application_status/<int:id>/', views.update_application_status, name='update_application_status'),
]
