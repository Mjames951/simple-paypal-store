# Generated by Django 5.1.5 on 2025-01-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0002_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
