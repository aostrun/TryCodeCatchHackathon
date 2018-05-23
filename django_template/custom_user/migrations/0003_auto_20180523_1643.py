# Generated by Django 2.0.5 on 2018-05-23 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20180518_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
        migrations.AddField(
            model_name='user',
            name='blood_type',
            field=models.CharField(choices=[('0-', '0-'), ('0+', '0+'), ('A-', 'A-'), ('A+', 'A+'), ('B-', 'B-'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='distance',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='last_donation',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location_lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='location_lon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=30, null=True),
        ),
    ]
