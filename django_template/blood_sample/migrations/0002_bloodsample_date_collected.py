# Generated by Django 2.0.5 on 2018-05-24 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodsample',
            name='date_collected',
            field=models.DateTimeField(null=True),
        ),
    ]
