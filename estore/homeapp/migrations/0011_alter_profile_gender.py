# Generated by Django 4.2.3 on 2023-07-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0010_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default=None, max_length=100),
        ),
    ]