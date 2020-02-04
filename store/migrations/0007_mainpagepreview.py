# Generated by Django 2.2.9 on 2020-02-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_request_is_alive'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPagePreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('preview', models.ImageField(upload_to='images/')),
                ('description', models.TextField(default='')),
            ],
        ),
    ]