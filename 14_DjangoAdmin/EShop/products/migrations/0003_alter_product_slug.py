# Generated by Django 5.1.4 on 2025-02-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
