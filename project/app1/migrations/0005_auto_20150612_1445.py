# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.DeleteModel(
            name='Library',
        ),
    ]
