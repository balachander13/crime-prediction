# Generated by Django 5.1.7 on 2025-03-08 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='confidence',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='reports',
            name='prediction',
            field=models.IntegerField(default=0),
        ),
    ]
