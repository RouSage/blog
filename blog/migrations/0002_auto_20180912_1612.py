# Generated by Django 2.1.1 on 2018-09-12 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 12, 13, 12, 16, 911279, tzinfo=utc), verbose_name='created at'),
        ),
        migrations.AlterField(
            model_name='category',
            name='url_slug',
            field=models.CharField(db_index=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='url_slug',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
