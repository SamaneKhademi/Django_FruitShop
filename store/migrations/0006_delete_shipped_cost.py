# Generated by Django 5.1 on 2024-08-25 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_shipped_cost_shipped_cost_shipped_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Shipped_cost',
        ),
    ]
