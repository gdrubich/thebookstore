# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class BookLoan(models.Model):
    book = models.ForeignKey('books.BookInstance', related_name='loans')
    user = models.ForeignKey(User)
    date = models.DateField()
    return_date = models.DateField()

    def __unicode__(self):
        return '{} {}'.format(self.book, self.user)


class Devolution(models.Model):
    STATES = (
        ('ontime', 'On Time'),
        ('late', 'Late'),
    )
    loan = models.ForeignKey('loans.BookLoan')
    status = models.CharField(choices=STATES, max_length=20)

    def __unicode__(self):
        return '{} {}'.format(self.loan, self.status)
