# Generated by Django 3.2.4 on 2021-10-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='speciality',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
