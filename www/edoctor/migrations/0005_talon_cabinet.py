# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edoctor', '0004_auto_20170326_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='talon',
            name='cabinet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
