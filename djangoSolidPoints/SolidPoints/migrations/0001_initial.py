# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=200000)),
                ('summary_text', models.CharField(max_length=100000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
