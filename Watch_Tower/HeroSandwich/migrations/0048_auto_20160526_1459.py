# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0047_auto_20160526_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='create',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2016, 5, 26, 14, 59, 56, 162157, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.Description'),
        ),
    ]
