# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django_countries.fields import CountryField

from django.contrib.auth.models import User


def cover_upload_path(instance, filename):
    return '/'.join(['cover', instance.genre.name, filename])


class Book(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)
    isbn = models.CharField(max_length=25)
    pages = models.IntegerField()
    author = models.ForeignKey('books.Author', related_name='books')
    genre = models.ForeignKey('books.Genre')
    language = models.ForeignKey('books.Language')
    cover_img = models.ImageField(
        upload_to=cover_upload_path, default='/cover/default_cover.jpeg', null=True)

    # class Meta:
    #   pass
    @property
    def available(self):
        return self.instances.filter(status='av').count() > 0

    def __unicode__(self):
        return '{}'.format(self.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField()
    country = CountryField()

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return '{}'.format(self.name)


class Language(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return '{}'.format(self.name)


class BookInstance(models.Model):
    STATES = (
        ('av', 'Available'),
        ('ret', 'Retired'),
        ('res', 'Reserved'),
    )
    unique_id = models.CharField(max_length=10)
    book = models.ForeignKey('books.Book', related_name='instances')
    status = models.CharField(choices=STATES, max_length=20)

    def __unicode__(self):
        return '{} {}'.format(self.book, self.unique_id)


@property
def is_librarian(self):
    return self.has_perm("loans.add_bookloan")


User.add_to_class("is_librarian", is_librarian)
