# Generated by Django 4.0.2 on 2022-03-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_remove_order_status_alter_order_order_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('order_placed', 'order placed'), ('item_shipped', 'item shipped'), ('order_deliverd', 'order deliverd'), ('order_cancelled', 'order cancelled')], default='order placed', max_length=50, null=True),
        ),
    ]
