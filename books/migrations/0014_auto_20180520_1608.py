# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0013_auto_20180316_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
                ('created_by', models.ForeignKey(default=1, related_name='Item', to=settings.AUTH_USER_MODEL)),
                ('tax_rate', models.ForeignKey(to='books.TaxRate')),
            ],
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='item',
            field=models.ForeignKey(blank=True, null=True, default=1, to='books.Item'),
        ),
    ]
