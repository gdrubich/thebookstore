# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-19 14:56
from __future__ import unicode_literals

import books.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_bookinstance_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_img',
            field=models.ImageField(default='/cover/default_cover.jpeg', null=True, upload_to=books.models.cover_upload_path),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='books.Book'),
        ),
    ]