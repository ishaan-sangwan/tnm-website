# Generated by Django 5.0 on 2024-03-11 09:04

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_remove_participation_particpant_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='participation',
            name='p_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
