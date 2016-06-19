# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hismaxdb', '0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_code', models.IntegerField(db_column='AREA_CODE', primary_key=True, serialize=False)),
                ('main_name', models.CharField(db_column='MAIN_NAME', max_length=12)),
                ('zip_code', models.IntegerField(blank=True, db_column='ZIP_CODE', null=True)),
                ('tel_code', models.CharField(blank=True, db_column='TEL_CODE', max_length=3, null=True)),
                ('keyin_date', models.CharField(db_column='KEYIN_DATE', max_length=7)),
                ('keyin_clerk', models.CharField(db_column='KEYIN_CLERK', max_length=6)),
                ('heaf_code', models.CharField(blank=True, db_column='HEAF_CODE', max_length=4, null=True)),
                ('old_main_name', models.CharField(blank=True, db_column='OLD_MAIN_NAME', max_length=40, null=True)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pttype',
            fields=[
                ('pt_type', models.IntegerField(db_column='PT_TYPE', primary_key=True, serialize=False)),
                ('type_name', models.CharField(db_column='TYPE_NAME', max_length=10)),
                ('price_type', models.IntegerField(blank=True, db_column='PRICE_TYPE', null=True)),
                ('keyin_date', models.CharField(db_column='KEYIN_DATE', max_length=7)),
                ('keyin_clerk', models.CharField(db_column='KEYIN_CLERK', max_length=6)),
            ],
            options={
                'db_table': 'pttype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegisterDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chart_no', models.IntegerField(db_column='CHART_NO')),
                ('birth_date', models.CharField(blank=True, db_column='BIRTH_DATE', max_length=7, null=True)),
                ('registration_id', models.TextField(db_column='REGISTRATION_ID', max_length=250)),
                ('register_datetime', models.DateTimeField(auto_now_add=True, db_column='REGISTER_DATETIME')),
                ('eff_flag', models.CharField(db_column='EFF_FLAG', max_length=1)),
            ],
            options={
                'db_table': 'RegisterDevice',
                'managed': False,
            },
        ),
    ]
