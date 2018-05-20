# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20180303_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='address_line_1',
            field=models.CharField(max_length=128, default=datetime.datetime(2018, 3, 16, 17, 11, 56, 443861, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='address_line_2',
            field=models.CharField(max_length=128, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.CharField(max_length=64, default=datetime.datetime(2018, 3, 16, 17, 12, 1, 629914, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='country',
            field=models.CharField(max_length=50, default=datetime.datetime(2018, 3, 16, 17, 12, 13, 230158, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='postal_code',
            field=models.CharField(max_length=256, default=datetime.datetime(2018, 3, 16, 17, 12, 20, 541040, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
