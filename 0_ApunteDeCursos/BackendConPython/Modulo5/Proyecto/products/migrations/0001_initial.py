# Generated by Django 5.1.1 on 2024-09-21 23:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/products')),
                ('discount', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
