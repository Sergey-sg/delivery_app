# Generated by Django 4.0.6 on 2022-07-10 07:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_is_processed',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='customer name', max_length=250, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='name')),
                ('email', models.EmailField(help_text='used for feedback', max_length=254, verbose_name='email')),
                ('phone', models.CharField(help_text='used for feedback', max_length=13, validators=[django.core.validators.RegexValidator(message='The phone number must be in the format: "+380999999999". Starts with "+380" and 9 digits.', regex='^\\+380\\d{9}')], verbose_name='phone number')),
                ('address', models.CharField(help_text='shipping address', max_length=500, verbose_name='address')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
