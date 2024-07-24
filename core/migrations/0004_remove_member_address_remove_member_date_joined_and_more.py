# Generated by Django 5.0.7 on 2024-07-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_member_address_member_date_joined_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='address',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
