# Generated by Django 5.1.7 on 2025-03-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_reports_confidence_reports_prediction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reports',
            old_name='crimeType',
            new_name='crime_type',
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='daysAfterReported',
            new_name='days_after_reported',
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='reportedDelay',
            new_name='reported_delay',
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='timeOfCrime',
            new_name='time_of_crime',
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='victimDescent',
            new_name='victim_descent',
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='victimSex',
            new_name='victim_sex',
        ),
        migrations.RenameField(
            model_name='reports',
            old_name='weaponUsed',
            new_name='weapon_used',
        ),
        migrations.AddField(
            model_name='reports',
            name='area_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='crime_type_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='victim_descent_label',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='victim_sex_label',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reports',
            name='weapon_used_label',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
