# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtrial', '0002_center_ecrf'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='center',
            field=models.ForeignKey(default=1, to='webtrial.Center'),
        ),
    ]
