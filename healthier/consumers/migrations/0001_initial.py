# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-12 13:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('healthier_ID', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(blank=True, choices=[('', 'Select Gender'), ('M', 'Male'), ('F', 'Female')], max_length=5)),
                ('text', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, null=True, upload_to=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]