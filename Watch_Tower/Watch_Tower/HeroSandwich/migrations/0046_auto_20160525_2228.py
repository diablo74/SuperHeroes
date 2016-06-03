# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 22:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0045_auto_20160525_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='age_now',
        ),
        migrations.AddField(
            model_name='description',
            name='birth_date',
            field=models.DateField(default=datetime.datetime(2016, 5, 25, 22, 28, 33, 130023, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.Description'),
        ),
    ]