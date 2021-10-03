from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from .models import *
from .forms import *

# Логика входа в админку
def login_admin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = User.objects.get(email=cd['email'])
            print(username)
            user = authenticate(username=username, password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if user.is_superuser:
                        return redirect('admin')
                    else:
                        return redirect('')
            else:
                return render(request, 'account/login_error.html')
    else:
        form = LoginForm()
    return render(request, 'adminpanel/login.html', {'form': form})

def logout_admin(request):
        logout(request)
        return redirect('login_admin')

def website_main(request):
    data = {
        'about': About.objects.all().first(),
        'teams': Team.objects.all(),
        'portfolio': Portfolio.objects.all().first(),
        'projects': Project.objects.all(),
    }
    return render(request, 'adminpanel/website/index.html', data)

def admin(request):
    return  render(request, 'adminpanel/statistics.html')

def about(request):
    about_info = About.objects.all().first()
    teams = Team.objects.all()
    num_extra = 3 - teams.count()
    team_from = modelformset_factory(Team, form=TeamForm, extra=num_extra)

    if request.method == "POST":
        print(request.POST)
        about_info_form = AboutForm(request.POST, request.FILES, instance=about_info)
        formset = team_from(request.POST, request.FILES, queryset=teams)
        if about_info_form.is_valid():
            about_info_form.save()

        print(formset)
        if formset.is_valid():
            formset.save()
        else:
            print('Формсет не валидный ')
            print(formset.errors)

        return redirect('about')
    else:
        about_info_form = AboutForm(instance=about_info)
        formset = team_from(queryset=teams)

    data = {
        'about': about_info_form,
        'teams': formset
    }
    return render(request, 'adminpanel/maininfo/about.html', data)

def projects(request):
    portfolio = Portfolio.objects.all().first()
    project_list = Project.objects.all()

    if request.method == "POST":
        portfolio_form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if portfolio_form.is_valid():
            portfolio_form.save()

        return redirect('projects')
    else:
        portfolio_form = PortfolioForm(instance=portfolio)

    data = {
        'portfolio': portfolio_form,
        'project_list': project_list,
    }
    return render(request, 'adminpanel/maininfo/projects.html', data)

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('projects')
    else:
        form = ProjectForm()

    data = {
        'form': form,
    }
    return render(request, 'adminpanel/maininfo/create_project.html', data)