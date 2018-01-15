# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Book, BookInstance, Genre, Author, Language


class BookAdmin (admin.ModelAdmin):
    book_display = ('title', 'author')


class GenreAdmin (admin.ModelAdmin):
    genre_display = ('name')


class AuthorAdmin (admin.ModelAdmin):
    author_display = ('first_name', 'last_name')


class LanguageAdmin (admin.ModelAdmin):
    language_display = ('name')


class BookInstanceAdmin (admin.ModelAdmin):
    book_instance_display = ('book', 'unique_id')


admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
