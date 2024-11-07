# Generated by Django 5.1.1 on 2024-11-04 21:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_invoice_is_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicepayment',
            name='paid_amount',
            field=models.DecimalField(decimal_places=2, default=123, max_digits=8, validators=[django.core.validators.MinValueValidator(5000), django.core.validators.MaxValueValidator(10000000)], verbose_name='Paid amount'),
            preserve_default=False,
        ),
    ]
