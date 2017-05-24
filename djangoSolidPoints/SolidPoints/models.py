# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime
from django.utils import timezone

class VoiceEntry(models.Model):
    entry_text = models.CharField(max_length=200000)
    summary_text = models.CharField(max_length=100000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.entry_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


