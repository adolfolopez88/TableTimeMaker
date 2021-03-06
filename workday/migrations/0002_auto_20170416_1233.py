# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 02:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('workday', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkdayClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client')),
            ],
        ),
        migrations.AlterModelOptions(
            name='workday',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='workdayclient',
            name='workday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workday.Workday'),
        ),
    ]
