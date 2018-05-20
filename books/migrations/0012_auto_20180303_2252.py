# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_auto_20150324_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='organizations', to=settings.AUTH_USER_MODEL),
        ),
    ]
