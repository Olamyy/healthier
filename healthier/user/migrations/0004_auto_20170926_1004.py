# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-26 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170926_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthieruser',
            old_name='has_configure_account',
            new_name='has_configured_account',
        ),
    ]
