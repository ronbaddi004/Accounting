# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(verbose_name='To Client', to='people.Client'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='organization',
            field=models.ForeignKey(verbose_name='From Organization', related_name='invoices', to='books.Organization'),
        ),
        migrations.AddField(
            model_name='expenseclaimline',
            name='expense_claim',
            field=models.ForeignKey(related_name='lines', to='books.ExpenseClaim'),
        ),
        migrations.AddField(
            model_name='expenseclaimline',
            name='tax_rate',
            field=models.ForeignKey(to='books.TaxRate'),
        ),
        migrations.AddField(
            model_name='expenseclaim',
            name='employee',
            field=models.ForeignKey(verbose_name='Paid by employee', to='people.Employee'),
        ),
        migrations.AddField(
            model_name='expenseclaim',
            name='organization',
            field=models.ForeignKey(verbose_name='From Organization', related_name='expense_claims', to='books.Organization'),
        ),
        migrations.AddField(
            model_name='estimateline',
            name='invoice',
            field=models.ForeignKey(related_name='lines', to='books.Estimate'),
        ),
        migrations.AddField(
            model_name='estimateline',
            name='tax_rate',
            field=models.ForeignKey(to='books.TaxRate'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='client',
            field=models.ForeignKey(verbose_name='To Client', to='people.Client'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='organization',
            field=models.ForeignKey(verbose_name='From Organization', related_name='estimates', to='books.Organization'),
        ),
        migrations.AddField(
            model_name='billline',
            name='bill',
            field=models.ForeignKey(related_name='lines', to='books.Bill'),
        ),
        migrations.AddField(
            model_name='billline',
            name='tax_rate',
            field=models.ForeignKey(to='books.TaxRate'),
        ),
        migrations.AddField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(verbose_name='From Client', to='people.Client'),
        ),
        migrations.AddField(
            model_name='bill',
            name='organization',
            field=models.ForeignKey(verbose_name='To Organization', related_name='bills', to='books.Organization'),
        ),
        migrations.AlterUniqueTogether(
            name='invoice',
            unique_together=set([('number', 'organization')]),
        ),
        migrations.AlterUniqueTogether(
            name='expenseclaim',
            unique_together=set([('number', 'organization')]),
        ),
        migrations.AlterUniqueTogether(
            name='estimate',
            unique_together=set([('number', 'organization')]),
        ),
        migrations.AlterUniqueTogether(
            name='bill',
            unique_together=set([('number', 'organization')]),
        ),
    ]
