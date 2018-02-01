# -*- coding: utf-8 -*-
from django import forms
from .models import Book

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Field, HTML


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-bookForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Row(
                Div(Field('title', css_class="typeahead", autocomplete="off"),
                    title='Title', css_class="col-md-6"),
                Div('author', title='Author', css_class="col-md-6")
            ),
            HTML(""" <hr> """),
            Row(
                Div('pages', title="Pages", css_class="col-md-6"),
                Div('language', title="Language", css_class="col-md-6"),
            ),
        )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn',
                  'pages', 'author', 'genre', 'language', 'cover_img']
