# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'books/index.html', context)


def booklist(request):
    context = {}
    return render(request, 'books/booklist.html', context)
