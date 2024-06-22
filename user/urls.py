from django.urls import path
from user import views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('empdashboard/', views.empdashboard, name='empdashboard'),
    path('jobdashboard/', views.jobdashboard, name='jobdashboard'),
    path('list/', views.list, name='list'),
    path('delete/<int:id>/', views.delete_user, name='delete'),
    path('logout/',views.logout_view,name="logout"),
    path('home/',views.home,name="home"),
]