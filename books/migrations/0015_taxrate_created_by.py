# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0014_auto_20180520_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxrate',
            name='created_by',
            field=models.ForeignKey(default=1, related_name='TaxRate', to=settings.AUTH_USER_MODEL),
        ),
    ]
