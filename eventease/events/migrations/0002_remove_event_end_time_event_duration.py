# Generated by Django 5.1.7 on 2025-03-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
