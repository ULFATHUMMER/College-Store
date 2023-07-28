# Generated by Django 4.2.3 on 2023-07-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0019_department_course_profile_course_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='course',
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('cs', 'Computer sceince'), ('cm', 'Commerce'), ('ms', 'Medical sceince')], max_length=100),
        ),
    ]
