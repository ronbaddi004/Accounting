# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_taxrate_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceline',
            name='item',
            field=models.ForeignKey(blank=True, null=True, to='books.Item'),
        ),
    ]
