# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Book, BookInstance


@receiver(post_save, sender=Book)
def create_book_instance(sender, instance, created, **kwargs):
    if created:
        BookInstance.objects.create(book=instance)
