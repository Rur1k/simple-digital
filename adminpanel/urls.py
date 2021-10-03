from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('projects/create', views.project_create, name='project_create'),

    # Авторизация
    path('login/', views.login_admin, name='login_admin'),
    path('logout/', views.logout_admin, name='logout_admin'),
]