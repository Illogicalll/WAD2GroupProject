# Generated by Django 2.2.28 on 2023-03-13 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resell', '0006_auto_20230305_1748'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'cateName')},
        ),
    ]
