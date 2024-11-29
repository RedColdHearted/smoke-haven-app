# Generated by Django 5.1.1 on 2024-11-12 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0010_remove_invoice_payment_status'),
        ('products', '0002_alter_supplier_bik_alter_supplier_inn_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='products.supplier', verbose_name='Supplier id'),
        ),
    ]
