# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book, Author
from django.contrib.auth.models import Permission


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'books/index.html', context)


def booklist(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books/booklist.html', context)


def userlist(request):
    users = User.objects.all().exclude(id=request.user.id)
    for user in users:
        if user.is_librarian:
            users = users.exclude(id=user.id)
    context = {
        'users': users,
    }
    return render(request, 'books/userlist.html', context)


def edit_permission(request):
    if request.method == 'POST':
        error = []
        if not request.POST.get('value', None):
            error = "No hay cambios que guardar"
        user = get_object_or_404(User, pk=request.POST.get('user', 0))
        permission = Permission.objects.get(codename='add_bookloan')
        user.user_permissions.add(permission)
        return JsonResponse({'error': error})


def author_detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    context = {
        'author': author,
    }
    return render(request, 'books/author.html', context)
