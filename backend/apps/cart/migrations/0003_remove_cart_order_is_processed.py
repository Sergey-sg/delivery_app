# Generated by Django 4.0.6 on 2022-07-10 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_order_is_processed_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_is_processed',
        ),
    ]