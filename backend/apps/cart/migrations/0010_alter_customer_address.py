# Generated by Django 4.0.6 on 2022-07-11 20:01

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200),
        ),
    ]
