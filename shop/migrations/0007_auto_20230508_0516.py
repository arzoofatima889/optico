# Generated by Django 3.0 on 2023-05-08 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20230504_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='purchase_order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='Remarks',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Purchase_order_Detail_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('products', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Products')),
            ],
        ),
    ]