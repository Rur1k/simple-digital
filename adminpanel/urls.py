from django.urls import path
from adminpanel import views

urlpatterns = [
    path('', views.admin, name='admin'),

    # Авторизация
    path('login/', views.login_admin, name='login_admin'),
    path('logout/', views.logout_admin, name='logout_admin'),
]