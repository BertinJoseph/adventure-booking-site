# Generated by Django 5.0.2 on 2024-03-29 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_adventurepackage_accommodation_price_per_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adventurepackage',
            name='accommodation_price_per_person',
        ),
    ]
