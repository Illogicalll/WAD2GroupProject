# Generated by Django 4.1.5 on 2023-03-18 18:58

from django.db import migrations, models
import resell.models


class Migration(migrations.Migration):

    dependencies = [
        ('resell', '0006_remove_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True),
        ),
    ]
