# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-28 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0004_auto_20170228_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='points',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.DecimalField(decimal_places=17, default=0, max_digits=20),
        ),
    ]