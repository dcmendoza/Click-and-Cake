# Generated by Django 5.1 on 2024-09-25 04:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.CharField(choices=[('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='medium', max_length=10)),
                ('flavor', models.CharField(choices=[('vanilla', 'Vanilla'), ('chocolate', 'Chocolate'), ('strawberry', 'Strawberry'), ('red_velvet', 'Red Velvet'), ('lemon', 'Lemon')], default='vanilla', max_length=20)),
                ('cream_flavor', models.CharField(choices=[('vanilla', 'Vanilla'), ('chocolate', 'Chocolate'), ('cream_cheese', 'Cream Cheese'), ('buttercream', 'Buttercream'), ('lemon', 'Lemon')], default='vanilla', max_length=20)),
                ('shape', models.CharField(choices=[('round', 'Round'), ('square', 'Square'), ('heart', 'Heart'), ('rectangle', 'Rectangle')], default='round', max_length=10)),
                ('toppings', models.JSONField(default=list)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img/cake/')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cake.cake')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
