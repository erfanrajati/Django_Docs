# Generated by Django 5.1.4 on 2025-02-09 19:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=16, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
