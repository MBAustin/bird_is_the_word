# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-01 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bird_quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='group',
            field=models.CharField(default=None, max_length=140),
            preserve_default=False,
        ),
    ]
