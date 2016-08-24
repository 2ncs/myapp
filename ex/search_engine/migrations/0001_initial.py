# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('perioxh', models.CharField(blank=True, max_length=128)),
                ('periferia', models.CharField(blank=True, max_length=128)),
                ('dieuthinsh', models.CharField(blank=True, max_length=128)),
                ('price', models.CharField(blank=True, max_length=128)),
                ('live_mousikh', models.NullBooleanField()),
                ('for_kids', models.NullBooleanField()),
                ('view', models.NullBooleanField()),
                ('romantic', models.NullBooleanField()),
                ('cozy', models.NullBooleanField()),
                ('stigma', models.URLField(blank=True)),
                ('butlair_link', models.URLField(blank=True)),
                ('site', models.URLField(blank=True)),
                ('e_table', models.NullBooleanField()),
                ('thl', models.CharField(blank=True, max_length=128)),
                ('comments', models.TextField(blank=True)),
                ('rate', models.FloatField(null=True)),
            ],
        ),
    ]