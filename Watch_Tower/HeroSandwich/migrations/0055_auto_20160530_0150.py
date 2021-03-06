# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0054_auto_20160527_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='photos',
            field=models.ManyToManyField(to='HeroSandwich.Photo'),
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.Description'),
        ),
    ]
