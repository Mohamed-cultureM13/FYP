# Generated by Django 3.0.5 on 2021-05-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalSide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('queue_id', models.UUIDField(primary_key=True, serialize=False)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('max_capacity', models.IntegerField()),
                ('address_id', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
