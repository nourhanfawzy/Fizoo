# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20150612_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='library',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]
