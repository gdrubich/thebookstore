# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book, Author
from .forms import BookForm
from django.contrib.auth.models import Permission
import services

from crispy_forms.helper import FormHelper


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


def booksearch(request):
    books_list = services.get_books(request.GET['q'])
    context = {
        'books_list': books_list,
    }
    return render(request, 'books/booksearch.html', context)


def book_admin(request):
    context = {}
    return render(request, 'books/book_admin.html', context)


def add_book(request):
    book_form = BookForm()
    # self.helper.add_input(Submit('submit', 'Submit'))
    # self.helper.add_input(Button('cancel', 'Cancel'))
    context = {
        'form': book_form,
    }
    return render(request, 'books/add_book.html', context)


def searchjson(request):
    books_list = services.get_books(request.GET['query'])
    if not books_list:
        return JsonResponse({})
    result = []
    for item in books_list['result']:
        info = item['volumeInfo']
        result.append({
            'title': info['title'],
            'subtitle': info.get('subtitle', ''),
            'id': item['id'],
        })
    return JsonResponse(result, safe=False)


def search_per_id(request):
    book = services.get_books(request.GET['id'])
    if not book:
        return JsonResponse({})
    info = book['result'][0]['volumeInfo']
    fields_to_show = {
        'author': info['authors'][0],
        'pages': info['pageCount'],
        'language': info['language'],
        'img_src': info['imageLinks']['smallThumbnail'],
    }

    return JsonResponse(fields_to_show)


def edit_book(request):
    pass


def delete_book(request):
    pass


def author_detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    context = {
        'author': author,
    }
    return render(request, 'books/author.html', context)
