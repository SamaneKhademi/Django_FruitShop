# Generated by Django 5.1 on 2024-08-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_blogpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipped_cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipped_cost', models.DecimalField(decimal_places=0, default=0, max_digits=12)),
            ],
        ),
    ]
