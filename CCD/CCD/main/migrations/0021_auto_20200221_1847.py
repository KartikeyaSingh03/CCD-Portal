# Generated by Django 3.0.3 on 2020-02-21 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_candidate_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
