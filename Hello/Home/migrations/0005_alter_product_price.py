# Generated by Django 4.1.7 on 2023-03-22 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_rename_complete_order_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
