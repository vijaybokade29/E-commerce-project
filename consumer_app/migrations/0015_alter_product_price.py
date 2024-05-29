# Generated by Django 5.0.1 on 2024-05-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_app', '0014_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=500, max_digits=6),
        ),
    ]
