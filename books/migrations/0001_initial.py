# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.checks
import datetime
from decimal import Decimal
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField(db_index=True, default=1)),
                ('total_incl_tax', models.DecimalField(verbose_name='Total (inc. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('total_excl_tax', models.DecimalField(verbose_name='Total (excl. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('date_issued', models.DateField(default=datetime.date.today)),
                ('date_dued', models.DateField(verbose_name='Due date', blank=True, null=True, help_text='The date when the total amount should have been collected')),
                ('date_paid', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-number',),
            },
            bases=(libs.checks.CheckingModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BillLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Estimate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField(db_index=True, default=1)),
                ('total_incl_tax', models.DecimalField(verbose_name='Total (inc. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('total_excl_tax', models.DecimalField(verbose_name='Total (excl. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('date_issued', models.DateField(default=datetime.date.today)),
                ('date_dued', models.DateField(verbose_name='Due date', blank=True, null=True, help_text='The date when the total amount should have been collected')),
                ('date_paid', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-number',),
            },
            bases=(libs.checks.CheckingModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EstimateLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseClaim',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField(db_index=True, default=1)),
                ('total_incl_tax', models.DecimalField(verbose_name='Total (inc. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('total_excl_tax', models.DecimalField(verbose_name='Total (excl. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('date_issued', models.DateField(default=datetime.date.today)),
                ('date_dued', models.DateField(verbose_name='Due date', blank=True, null=True, help_text='The date when the total amount should have been collected')),
                ('date_paid', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-number',),
            },
            bases=(libs.checks.CheckingModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ExpenseClaimLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.IntegerField(db_index=True, default=1)),
                ('total_incl_tax', models.DecimalField(verbose_name='Total (inc. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('total_excl_tax', models.DecimalField(verbose_name='Total (excl. tax)', default=Decimal('0'), max_digits=12, decimal_places=2)),
                ('date_issued', models.DateField(default=datetime.date.today)),
                ('date_dued', models.DateField(verbose_name='Due date', blank=True, null=True, help_text='The date when the total amount should have been collected')),
                ('date_paid', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-number',),
            },
            bases=(libs.checks.CheckingModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('label', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
                ('invoice', models.ForeignKey(related_name='lines', to='books.Invoice')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit_price_excl_tax', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.DecimalField(default=1, max_digits=8, decimal_places=2)),
                ('created_by', models.ForeignKey(default=1, related_name='Item', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('display_name', models.CharField(max_length=150, help_text='Name that you communicate')),
                ('legal_name', models.CharField(max_length=150, help_text='Official name to appear on your reports, sales invoices and bills')),
                ('address_line_1', models.CharField(max_length=128, blank=True, null=True)),
                ('address_line_2', models.CharField(max_length=128, blank=True, null=True)),
                ('city', models.CharField(max_length=64, default=0)),
                ('postal_code', models.CharField(max_length=256, default=1)),
                ('country', models.CharField(max_length=50, default='India')),
                ('members', models.ManyToManyField(related_name='organizations', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='owned_organizations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=12, decimal_places=2)),
                ('detail', models.CharField(max_length=255, blank=True, null=True)),
                ('date_paid', models.DateField(default=datetime.date.today)),
                ('reference', models.CharField(max_length=255, blank=True, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('-date_paid',),
            },
        ),
        migrations.CreateModel(
            name='TaxRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('rate', models.DecimalField(validators=[django.core.validators.MinValueValidator(Decimal('0')), django.core.validators.MaxValueValidator(Decimal('1'))], max_digits=6, decimal_places=5)),
                ('created_by', models.ForeignKey(default=1, related_name='TaxRate', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(verbose_name='Attached to Organization', related_name='tax_rates', to='books.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tax_rate',
            field=models.ForeignKey(to='books.TaxRate'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='item',
            field=models.ForeignKey(blank=True, null=True, to='books.Item'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='tax_rate',
            field=models.ForeignKey(to='books.TaxRate'),
        ),
    ]
