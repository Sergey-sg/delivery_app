# Generated by Django 4.0.6 on 2022-07-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, help_text='product quantity in stock', null=True, verbose_name='stock'),
        ),
    ]