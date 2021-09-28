from django.contrib import admin
from django.urls import path, include
from adminpanel import views


urlpatterns = [
    path('', views.website_main, name='main_page'),
    path('admin/', include('adminpanel.urls')),
]