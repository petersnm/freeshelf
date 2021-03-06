# Generated by Django 2.1.7 on 2019-03-16 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_book_favorited_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcategory',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookcategory',
            name='name',
            field=models.CharField(blank=True, help_text='Enter a book category (e.g. Django)', max_length=200),
        ),
    ]
