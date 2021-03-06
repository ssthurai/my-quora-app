# Generated by Django 2.2.2 on 2019-07-01 11:17

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0002_auto_20190701_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 29, 556976), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 29, 556996), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 29, 555786), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 29, 557688), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 29, 557708), null=True),
        ),
    ]
