# -*- coding: utf-8 -*-
import requests


def get_books(title):
    # import ipdb
    # ipdb.set_trace()
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'q': title}
    r = requests.get(url, params=params)
    result = r.json()
    books_list = {'result': result['items']}
    return books_list
