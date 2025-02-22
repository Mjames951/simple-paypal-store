# Generated by Django 5.1.5 on 2025-01-23 01:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField(null=True)),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
    ]
