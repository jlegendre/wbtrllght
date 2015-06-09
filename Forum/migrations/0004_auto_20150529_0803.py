# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0003_auto_20150529_0739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reply_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='id_patient',
        ),
        migrations.AddField(
            model_name='reply',
            name='patient',
            field=models.ForeignKey(to='Forum.Patient'),
        ),
        migrations.AddField(
            model_name='reply',
            name='question',
            field=models.ForeignKey(to='Forum.Question'),
        ),
    ]
