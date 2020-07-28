# Generated by Django 2.2.1 on 2019-06-28 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookitup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookingform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First', models.CharField(max_length=100)),
                ('Last', models.CharField(max_length=100)),
                ('Phone', models.IntegerField(max_length=10)),
                ('Email', models.CharField(max_length=100)),
                ('Arriving', models.CharField(max_length=100)),
                ('Departure', models.CharField(max_length=100)),
                ('adults', models.IntegerField(max_length=10)),
                ('children', models.IntegerField(max_length=10)),
                ('questions', models.TextField()),
            ],
        ),
    ]
