# Generated by Django 5.0 on 2024-02-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('event_id', models.IntegerField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=20)),
                ('event_date', models.DateTimeField()),
                ('event_incharge', models.CharField(max_length=20)),
            ],
        ),
    ]
