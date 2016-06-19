# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hismaxdb', '0002_auto_20160512_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientServicelist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('location_code', models.CharField(db_column='LOCATION_CODE', max_length=5)),
                ('view_date', models.CharField(db_column='VIEW_DATE', max_length=7)),
                ('apn', models.IntegerField(blank=True, db_column='APN', null=True)),
                ('seq_no', models.IntegerField(blank=True, db_column='SEQ_NO', null=True)),
                ('chart_no', models.IntegerField(blank=True, db_column='CHART_NO', null=True)),
                ('pt_name', models.CharField(blank=True, db_column='PT_NAME', max_length=100, null=True)),
                ('eff_flag', models.CharField(blank=True, db_column='EFF_FLAG', max_length=1, null=True)),
            ],
            options={
                'db_table': 'patient_servicelist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientServiceno',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('location_code', models.CharField(blank=True, db_column='LOCATION_CODE', max_length=5, null=True)),
                ('current_no', models.IntegerField(blank=True, db_column='CURRENT_NO', null=True)),
            ],
            options={
                'db_table': 'patient_serviceno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seqno',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, db_column='CODE', max_length=2, null=True)),
                ('seqno', models.IntegerField(blank=True, db_column='SEQNO', null=True)),
            ],
            options={
                'db_table': 'seqno',
                'managed': False,
            },
        ),
    ]
