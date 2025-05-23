# Generated by Django 5.1.6 on 2025-02-23 10:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budgets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='recurringexpense',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recurring_expenses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expense',
            name='currency',
            field=models.CharField(default='INR', max_length=10),
        ),
    ]
