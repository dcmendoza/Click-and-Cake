# Generated by Django 5.1 on 2024-11-13 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cake_quantities',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]