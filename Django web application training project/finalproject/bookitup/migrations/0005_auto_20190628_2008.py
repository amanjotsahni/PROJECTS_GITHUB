# Generated by Django 2.2.1 on 2019-06-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookitup', '0004_auto_20190628_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='adults',
            field=models.IntegerField(),
        ),
    ]