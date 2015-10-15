# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(default=b'INHERIT', help_text='The template used to render the content.', max_length=500, verbose_name='template'),
            preserve_default=True,
        ),
    ]
