# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 18:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_auto_20170623_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='user_tag',
        ),
    ]
