# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180619_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(verbose_name='To Client', default=1, to='people.Client'),
        ),
    ]
