# Generated by Django 4.0.6 on 2022-07-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=34, help_text='total price of order', max_digits=10, verbose_name='total price'),
            preserve_default=False,
        ),
    ]
