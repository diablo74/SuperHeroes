# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0040_auto_20160524_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.Description'),
        ),
    ]
