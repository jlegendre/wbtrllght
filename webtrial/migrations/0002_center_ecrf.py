# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtrial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center_number', models.CharField(max_length=50)),
                ('center_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ecrf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ecrf_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField(verbose_name=b'Start date')),
                ('end_date', models.DateTimeField(verbose_name=b'End date')),
                ('theoritical_number_of_patients', models.CharField(max_length=50)),
            ],
        ),
    ]
