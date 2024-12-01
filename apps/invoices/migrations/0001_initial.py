# Generated by Django 5.1.1 on 2024-11-30 13:35

import apps.invoices.models.utils
import config.common.paths
import django.core.validators
import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField(verbose_name='Object ID')),
                ('file', models.FileField(upload_to=config.common.paths._default_media_path)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('amount_to_pay', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(5000), django.core.validators.MaxValueValidator(10000000)], verbose_name='Amount')),
                ('deadline', models.DateField(default=apps.invoices.models.utils.generate_two_week_pass_date, verbose_name='Deadline')),
                ('is_expired', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Is expired')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='products.supplier', verbose_name='Supplier id')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='InvoicePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('paid_amount', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(5000), django.core.validators.MaxValueValidator(10000000)], verbose_name='Paid amount')),
                ('payment_type', models.CharField(choices=[('Cash', 'Cash'), ('Non cash', 'Non cash')], max_length=10, verbose_name='Payment type')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_payments', to='invoices.invoice', verbose_name='Invoice id')),
            ],
            options={
                'verbose_name': 'Invoice payment',
                'verbose_name_plural': 'Invoice payments',
            },
        ),
    ]
