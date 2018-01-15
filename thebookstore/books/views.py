# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'index.html', context)
