# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('HeroSandwich', '0076_auto_20160531_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', embed_video.fields.EmbedVideoField()),
            ],
        ),

    migrations.AlterModelOptions(
        name='description',
        options={'permissions': (('moderate_description', 'Can the user moderate description?'), ('view_unmoderated_description', 'Can the user view unmoderated description?'))},
    ),
    migrations.AlterField(
        model_name='character',
        name='description',
        field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='HeroSandwich.Description'),
    ),
    ]
