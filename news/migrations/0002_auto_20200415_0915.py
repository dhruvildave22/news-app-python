# Generated by Django 2.2.12 on 2020-04-15 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated_at',
        ),
    ]
