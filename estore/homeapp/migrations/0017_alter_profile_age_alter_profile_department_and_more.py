# Generated by Django 4.2.3 on 2023-07-27 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0016_alter_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=False, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('cs', 'Computer sceince'), ('cm', 'Commerce'), ('ms', 'Medical sceince')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.PositiveIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='purpose',
            field=models.CharField(choices=[('enquiry', 'Enquiry'), ('purchase', 'Purchase'), ('return', 'Return')], max_length=100),
        ),
    ]
