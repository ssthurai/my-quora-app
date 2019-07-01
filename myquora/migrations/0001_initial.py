# Generated by Django 2.2.2 on 2019-07-01 11:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(help_text='Write your answer here...', max_length=2000)),
                ('date_created', models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 12, 328245), null=True)),
                ('date_updated', models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 12, 328266), null=True)),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('date_created', models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 12, 326990), null=True)),
                ('credits', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(help_text='Enter your question in brief∂', max_length=1000)),
                ('date_created', models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 12, 328983), null=True)),
                ('date_updated', models.DateField(default=datetime.datetime(2019, 7, 1, 11, 17, 12, 329003), null=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myquora.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(help_text='Enter your comment...', max_length=1000)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_updated', models.DateField(blank=True, null=True)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myquora.Answer')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myquora.Author')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myquora.Author'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myquora.Question'),
        ),
    ]
