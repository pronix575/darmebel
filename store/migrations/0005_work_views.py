# Generated by Django 2.2.9 on 2020-02-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_request_is_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]