# Generated by Django 3.0 on 2023-05-09 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20230508_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='subtotal',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='total_items',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchase_order_detail_item',
            name='purchase_Order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Purchase_Order'),
        ),
    ]
