# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0013_auto_20160519_2153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SuperPower',
            new_name='Super_power',
        ),
        migrations.RenameField(
            model_name='super_power',
            old_name='superpower',
            new_name='super_power',
        ),
    ]
