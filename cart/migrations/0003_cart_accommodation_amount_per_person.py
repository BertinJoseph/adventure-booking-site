# Generated by Django 5.0.2 on 2024-03-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_cart_include_food_and_accommodation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='accommodation_amount_per_person',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
