# Generated by Django 3.0 on 2023-04-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230429_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='rack',
            field=models.CharField(blank=True, choices=[('', '-select-'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Rack',
        ),
    ]
