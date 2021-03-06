# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('initials', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name=b'date published')),
                ('modification_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
