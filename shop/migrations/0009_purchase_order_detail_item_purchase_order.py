# Generated by Django 3.0 on 2023-05-08 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20230508_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order_detail_item',
            name='purchase_Order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Purchase_Order'),
        ),
    ]
