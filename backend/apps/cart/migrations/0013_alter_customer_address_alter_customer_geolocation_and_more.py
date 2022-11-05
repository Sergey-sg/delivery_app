# Generated by Django 4.0.6 on 2022-07-13 11:18

from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_cartitem_sub_total_alter_cartitem_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=django_google_maps.fields.AddressField(help_text='address for delivery', max_length=200, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(help_text='geolocation of the customer', max_length=100, verbose_name='geolocation'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(help_text='communication with the Customer model', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='sent',
            field=models.BooleanField(default=False, help_text='order dispatch status', verbose_name='sent'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, help_text='total price of order', max_digits=12, verbose_name='total price'),
        ),
    ]