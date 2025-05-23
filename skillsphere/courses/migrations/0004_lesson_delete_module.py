# Generated by Django 5.1.7 on 2025-04-17 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_module_video_module_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('video_url', models.URLField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Module',
        ),
    ]
