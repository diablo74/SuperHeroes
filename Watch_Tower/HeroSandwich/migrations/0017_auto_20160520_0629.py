# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 06:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0016_auto_20160520_0514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='title',
            new_name='superhero',
        ),
    ]
