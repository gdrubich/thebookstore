# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Book, BookInstance


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'books/index.html', context)


def booklist(request):
    import ipdb
    ipdb.set_trace()
    books = Book.objects.all()
    av = 0

    def check_availability(book):
        if BookInstance.objects.filter(status='av'):
            return True
        else:
            return False

    for book in books:
        if check_availability(book):
            av += 1

    context = {
        'books': books,
        'av': av,
    }

    return render(request, 'books/booklist.html', context)
