# Generated by Django 2.1.7 on 2019-03-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190312_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='favorited_count',
            field=models.IntegerField(default=0),
        ),
    ]
