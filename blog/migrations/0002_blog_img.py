# Generated by Django 2.1.5 on 2019-02-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(default=1, upload_to=None),
            preserve_default=False,
        ),
    ]