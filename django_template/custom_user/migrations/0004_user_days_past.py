# Generated by Django 2.0.5 on 2018-05-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_auto_20180523_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='days_past',
            field=models.IntegerField(null=True),
        ),
    ]