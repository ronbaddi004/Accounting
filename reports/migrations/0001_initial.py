# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('business_type', models.CharField(max_length=50, choices=[('sole_proprietorship', 'Sole Proprietorship'), ('partnership', 'Partnership'), ('corporation', 'Corporation')])),
                ('organization', models.OneToOneField(blank=True, null=True, related_name='business_settings', to='books.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('financial_year_end_day', models.PositiveSmallIntegerField(default=31, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('financial_year_end_month', models.PositiveSmallIntegerField(default=12, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('tax_id_number', models.CharField(max_length=150, blank=True, null=True)),
                ('tax_id_display_name', models.CharField(max_length=150, blank=True, null=True)),
                ('tax_period', models.CharField(verbose_name='Tax Period', max_length=20, choices=[('monthly', '1 month'), ('bimonthly', '2 months'), ('quarter', '3 months'), ('half', '6 months'), ('year', '1 year')])),
                ('organization', models.OneToOneField(blank=True, null=True, related_name='financial_settings', to='books.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='PayRunSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('salaries_follow_profits', models.BooleanField(default=False)),
                ('payrun_period', models.CharField(verbose_name='Payrun Period', max_length=20, default='monthly', choices=[('monthly', 'monthly')])),
                ('organization', models.OneToOneField(blank=True, null=True, related_name='payrun_settings', to='books.Organization')),
            ],
        ),
    ]
