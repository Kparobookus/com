# Generated by Django 5.1.5 on 2025-03-05 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_candyshop', '0002_remove_product_author_remove_product_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='new_candyshop.category'),
        ),
    ]
