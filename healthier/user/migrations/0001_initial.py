# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.10.8 on 2017-09-27 08:39
=======
# Generated by Django 1.10.7 on 2017-09-27 10:03
>>>>>>> 847442984f916e30ea3417ba461349dedd6b1cd1
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthierUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('account_type', models.CharField(choices=[('PRO', 'Provider'), ('CON', 'Consumer')], max_length=3)),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('address', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('city', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('phone_number', models.CharField(max_length=200)),
                ('website', models.URLField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, verbose_name='Username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('is_logged_in', models.BooleanField(default=False, verbose_name='Logged In')),
                ('is_superuser', models.BooleanField(default=True, verbose_name='Superuser')),
                ('has_configured_account', models.BooleanField(default=False, verbose_name='Has Configured Account')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this hospital belongs to. An hospital will get all permissions granted to each of their groups.', related_name='hospital_set', related_query_name='hospital', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
