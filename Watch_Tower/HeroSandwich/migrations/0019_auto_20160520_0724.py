# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 07:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0018_superheropower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SuperHero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.RemoveField(
            model_name='superheropower',
            name='name',
        ),
        migrations.AddField(
            model_name='superheropower',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='superheropower',
            name='hero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.SuperHero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superheropower',
            name='power',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.Power'),
            preserve_default=False,
        ),
    ]
