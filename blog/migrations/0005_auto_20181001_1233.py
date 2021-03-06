# Generated by Django 2.1.1 on 2018-10-01 09:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180923_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 1, 9, 33, 16, 164525, tzinfo=utc), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2018, 10, 1, 9, 33, 16, 192528, tzinfo=utc), verbose_name='created ad'),
        ),
    ]
