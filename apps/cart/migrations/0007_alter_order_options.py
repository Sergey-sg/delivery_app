# Generated by Django 4.0.6 on 2022-07-11 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_remove_customer_cart'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'order', 'verbose_name_plural': 'Orders'},
        ),
    ]