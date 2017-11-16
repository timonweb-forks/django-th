# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_th', '0012_auto_20171003_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=255)),
                ('subreddit', models.CharField(max_length=80)),
                ('share_link', models.BooleanField(default=False)),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                              to='django_th.TriggerService')),
            ],
            options={
                'db_table': 'django_th_reddit',
            },
        ),
    ]
