# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Book, BookInstance

import unittest


from mixer.backend.django import mixer


class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1


class TestBasic2(unittest.TestCase):
    "Show setup and teardown"

    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def test_basic1(self):
        "Basic with setup"

        self.assertNotEqual(self.a, 2)

    def test_basic2(self):
        "Basic2 with setup"
        assert self.a != 2

    def test_fail(self):
        "This test should fail"
        assert self.a == 2


class BookTestCase(unittest.TestCase):
    "Book tests"

    def setUp(self):
        self.book1 = mixer.blend(Book)

    def test_instance_signal(self):
        "This also should faild"
        self.assertTrue(self.book1.instances.all().count() == 1, msg=None)

    def test_available_method(self):
        "Another test that fails"
        self.book1.instances.create(status='av')
        self.book1.instances.create(status='av')
        self.assertEqual(self.book1.available, True)



