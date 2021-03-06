# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 15:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_auto_20160611_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='tours/static/tours/img/photo')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Tour')),
            ],
        ),
    ]
