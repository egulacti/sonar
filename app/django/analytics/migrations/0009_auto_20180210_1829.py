# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-10 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20180210_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blereport',
            name='count',
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name='blereport',
            name='report_type',
            field=models.CharField(choices=[('H', 'Hour'), ('D', 'Day'), ('W', 'Week'), ('M', 'Month')], editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='blereport',
            name='timezone',
            field=models.CharField(editable=False, max_length=60),
        ),
    ]