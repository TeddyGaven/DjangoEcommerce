# Generated by Django 4.1.7 on 2023-03-22 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_order_shippingaddress_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='complete',
            new_name='completed',
        ),
    ]
