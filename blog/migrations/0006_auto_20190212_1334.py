# Generated by Django 2.1.5 on 2019-02-12 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190211_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]