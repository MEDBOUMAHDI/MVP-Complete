# Generated by Django 4.2.4 on 2023-09-01 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardio_calculator', '0003_healthdata_is_hypertensive'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskscore',
            name='risk_level',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]