# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名稱')),
                ('description', models.TextField(blank=True, default='', verbose_name='內容簡介')),
                ('original_price', models.PositiveIntegerField(default=0, verbose_name='原價')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='售價')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '未上架'), (1, '上架中'), (2, '已下架')], default=0, verbose_name='狀態')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='新增時間')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新時間')),
                ('published', models.DateTimeField(null=True, verbose_name='上架時間')),
                ('author', models.CharField(blank=True, default='', max_length=100, verbose_name='作者')),
                ('translator', models.CharField(blank=True, default='', max_length=100, verbose_name='譯者')),
                ('publisher', models.CharField(blank=True, default='', max_length=100, verbose_name='出版社')),
                ('isbn', models.CharField(blank=True, default='', max_length=13, verbose_name='ISBN')),
                ('language', models.CharField(blank=True, default='', max_length=20, verbose_name='語言')),
            ],
            options={
                'verbose_name': '書籍',
                'verbose_name_plural': '書籍',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分類名稱')),
            ],
            options={
                'verbose_name': '分類',
                'verbose_name_plural': '分類',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='標籤名稱')),
            ],
            options={
                'verbose_name': '標籤',
                'verbose_name_plural': '標籤',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.Category', verbose_name='分類'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='books.Tag', verbose_name='標籤'),
        ),
    ]
