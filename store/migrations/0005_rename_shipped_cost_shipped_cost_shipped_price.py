# Generated by Django 5.1 on 2024-08-25 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_shipped_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipped_cost',
            old_name='shipped_cost',
            new_name='shipped_price',
        ),
    ]
