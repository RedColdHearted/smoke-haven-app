# Generated by Django 5.1.1 on 2024-11-05 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0009_alter_invoicepayment_paid_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='payment_status',
        ),
    ]
