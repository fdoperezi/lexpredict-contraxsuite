# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 21:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lease', '0016_auto_20171219_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leasedocument',
            old_name='address_longtitude',
            new_name='address_longitude',
        ),
    ]
