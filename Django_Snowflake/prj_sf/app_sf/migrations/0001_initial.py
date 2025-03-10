# Generated by Django 5.1.6 on 2025-02-21 04:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('tripID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tripDuration', models.IntegerField()),
                ('tripDate', models.DateField()),
                ('boarding', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'trip',
            },
        ),
    ]
