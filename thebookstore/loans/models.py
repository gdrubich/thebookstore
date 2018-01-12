# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class BookLoan(models.Model):
    STATES = (
        ('av', 'Available'),
        ('ret', 'Retirado'),
        ('res', 'Reserved'),
    )
    due_back = models.DateField()
    status = models.CharField(choices=STATES, max_length=20)
    book = models.ForeignKey('books.BookInstance', related_name='loan')

    def __unicode__(self):
        return '{}'.format(self.book)
