# Generated by Django 5.0 on 2024-03-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_participation_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_discpription',
            field=models.TextField(null=True),
        ),
    ]
