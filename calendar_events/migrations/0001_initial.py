# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=400)),
                ('title', models.CharField(default='Blank Title', max_length=100)),
                ('event_time', models.DateField()),
                ('slug', models.SlugField(default='blank-title', max_length=200)),
            ],
        ),
    ]