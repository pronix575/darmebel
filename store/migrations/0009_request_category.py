# Generated by Django 2.2.9 on 2020-02-03 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.Category'),
        ),
    ]