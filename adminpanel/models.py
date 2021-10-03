from django.db import models


# class MainPageInfo(models.Model):
#     id = models.AutoField(unique=True, primary_key=True)
#     title = models.CharField('Заголовок', max_length=64, null=True, blank=True)
#     description = models.TextField('Краткий текст', null=True, blank=True)
#     image = models.ImageField(upload_to='', null=True, blank=True)

class About(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    description = models.TextField('Инфорамция о нас', null=True, blank=True)

class Team(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    speciality = models.CharField(max_length=128, null=True, blank=True)
    photo = models.ImageField(upload_to='static/adminpanel/img/team', null=True, blank=True)

class Portfolio(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    description = models.TextField('Инфорамция о портфолио', null=True, blank=True)

class Project(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name_project = models.CharField('Имя проекта', max_length=64, null=True, blank=True)
    main_image = models.ImageField(upload_to='static/img/website/projects', null=True, blank=True)

class Service(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    service_name = models.CharField('Имя услуги', max_length=64, null=True, blank=True)
    description = models.TextField('Инфорамция о услуге', null=True, blank=True)

class Country(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    country_name = models.CharField('Имя услуги', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.country_name

class Status(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    status_name = models.CharField('Имя услуги', max_length=64, null=True, blank=True)

    def __str__(self):
        return self.status_name

class Feedback(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField('Имя заказчика', max_length=128, null=True, blank=True)
    email = models.EmailField(null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)


