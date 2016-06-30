# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 13:01
# flake8: noqa
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_feeds', '0002_auto_20160620_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_app_label',
            field=models.CharField(blank=True, help_text=b'blog App whose Feed is to be generated', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_author_email',
            field=models.EmailField(blank=True, help_text=b'Email of author', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_author_link',
            field=models.URLField(blank=True, help_text=b'Link of author', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_description',
            field=models.CharField(blank=True, help_text=b'Description of field', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_item_content_field',
            field=models.CharField(blank=True, help_text=b'Content Field for feed item', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_item_description_field',
            field=models.CharField(blank=True, help_text=b'Description field for feed item', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_link',
            field=models.URLField(blank=True, help_text=b'link for Feed', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_model_name',
            field=models.CharField(blank=True, help_text=b'Model to be used for feed generation', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='feedsappsettings',
            name='feed_title',
            field=models.CharField(blank=True, help_text=b'Title of Feed', max_length=255, null=True),
        ),
    ]
