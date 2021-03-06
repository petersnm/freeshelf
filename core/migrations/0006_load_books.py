# Generated by Django 2.1.7 on 2019-03-16 21:35

from django.db import migrations
from django.conf import settings
import os.path
import csv
from django.utils.text import slugify

def load_book_data(apps, schema_editor):
    """
    Read a CSV file full of books and insert them into the database.
    """
    Book = apps.get_model('core', 'Book')
    BookCategory = apps.get_model('core', 'BookCategory')

    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'books.csv')
    with open(datafile, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            book_title = row['title']
            # Don't create a book if title matches an existing Book record
            if Book.objects.filter(title=book_title).count():
                continue
            # print(row, file=open('file.txt', 'w'))
            if not row['book_categories']:
                categories, _ = BookCategory.objects.get_or_create(name='No Category', slug="no-category")
                categories = [categories]
            else: 
                categories = []
                category_list = [i.strip() for i in row['book_categories'].split('/')]
                for i in category_list:
                    new_category, _ = BookCategory.objects.get_or_create(name=i, slug=slugify(i))
                    categories.append(new_category)

            book = Book.objects.create(
                title = row['title'],
                author = row['author'],
                book_description = row['book_description'],
                book_url = row['book_url'],
                slug=slugify(row['title'])[:50]
            )            
            
            for i in categories:
                book.book_categories.add(i)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190316_1725'),
    ]

    operations = [
        migrations.RunPython(load_book_data),
    ]
