# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
            options={
                'ordering': ['-added_at'],
                'db_table': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('added_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-added_at'],
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(related_name='question_author_id', to='qa.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(to='qa.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(to='qa.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(to='qa.Question'),
        ),
    ]
