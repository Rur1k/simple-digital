from django.contrib.auth.models import User
from django import forms
from .models import *

# Формы авторизации
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'E-mail или ID',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

# Формы админки
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['id', 'description']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'speciality',
            'photo'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'speciality': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['id', 'description']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'name_project', 'main_image', 'description']
        widgets = {
            'name_project': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'main_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['id', 'service_name', 'description']
        widgets = {
            'service_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['id', 'country_name']
        widgets = {
            'country_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['id', 'status_name']
        widgets = {
            'status_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

# ФОрма для сайта

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'email', 'country', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'country': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }