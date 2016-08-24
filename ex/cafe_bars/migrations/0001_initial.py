# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-11 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Beer_pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cafe_Bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dieuthinsh', models.CharField(max_length=128)),
                ('perioxh', models.CharField(max_length=128)),
                ('thl', models.CharField(max_length=128)),
                ('perigrafh', models.TextField(blank=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='cafe_bars/static/tours/img/logo')),
                ('photo', models.FileField(blank=True, null=True, upload_to='cafe_bars/static/tours/img/photo')),
                ('site', models.URLField(blank=True)),
                ('butlair_link', models.URLField(blank=True)),
                ('roof', models.NullBooleanField()),
                ('garden', models.NullBooleanField()),
                ('romantic', models.NullBooleanField()),
                ('view', models.NullBooleanField()),
                ('gay_lesbian', models.NullBooleanField()),
                ('dance', models.NullBooleanField()),
                ('rock', models.NullBooleanField()),
                ('techno', models.NullBooleanField()),
                ('rempetiko_ellhniko', models.NullBooleanField()),
                ('jazz', models.NullBooleanField()),
                ('chill', models.NullBooleanField()),
                ('whiskes', models.NullBooleanField()),
                ('mpouzoukia', models.NullBooleanField()),
                ('live_music', models.NullBooleanField()),
                ('beach_bar', models.NullBooleanField()),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_bars.Cafe_Bar')),
            ],
        ),
        migrations.CreateModel(
            name='Cocktail_bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_bars.Cafe_Bar')),
            ],
        ),
        migrations.CreateModel(
            name='Wine_bar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_bars.Cafe_Bar')),
            ],
        ),
        migrations.AddField(
            model_name='cafe',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_bars.Cafe_Bar'),
        ),
        migrations.AddField(
            model_name='beer_pub',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_bars.Cafe_Bar'),
        ),
        migrations.AddField(
            model_name='bar',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_bars.Cafe_Bar'),
        ),
    ]
