# Generated by Django 2.2.9 on 2020-01-02 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_work_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Work')),
            ],
        ),
    ]