# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 08:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0030_character_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='publish_date',
        ),
    ]
