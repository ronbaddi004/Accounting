# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=150)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(max_length=128, blank=True, null=True)),
                ('city', models.CharField(max_length=64)),
                ('postal_code', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(related_name='clients', to='books.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('payroll_tax_rate', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('1'))], max_digits=6, decimal_places=5)),
                ('salary_follows_profits', models.BooleanField(default=False)),
                ('shares_percentage', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('1'))], max_digits=6, decimal_places=5)),
                ('organization', models.ForeignKey(related_name='employees', to='books.Organization')),
            ],
        ),
    ]
