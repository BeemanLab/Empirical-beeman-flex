# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-10 17:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0014_auto_20160607_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('groupToken', models.CharField(max_length=100)),
                ('recycle', models.BooleanField(default=True)),
                ('unique_id', models.BooleanField(default=True)),
                ('groupSessions', models.TextField(default=b'')),
                ('numTokens', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(300), django.core.validators.MinValueValidator(1)])),
                ('totalTokens', models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(1)])),
                ('user', models.CharField(max_length=100)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tokengeneration',
            name='studyName',
        ),
        migrations.RemoveField(
            model_name='session',
            name='expName',
        ),
        migrations.RemoveField(
            model_name='study',
            name='recycle',
        ),
        migrations.RemoveField(
            model_name='study',
            name='unique_id',
        ),
        migrations.AddField(
            model_name='session',
            name='user',
            field=models.CharField(default='NotSpecified', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='study',
            name='appletName',
            field=models.CharField(default='NoApplet.html', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TokenGeneration',
        ),
        migrations.AddField(
            model_name='experiment',
            name='study',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exp.Study'),
        ),
        migrations.AddField(
            model_name='session',
            name='exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exp.Experiment'),
        ),
    ]
