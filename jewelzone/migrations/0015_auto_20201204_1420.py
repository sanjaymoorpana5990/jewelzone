# Generated by Django 3.1.3 on 2020-12-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelzone', '0014_auto_20201204_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.CharField(max_length=10),
        ),
    ]