# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('cellphone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('model_pic', models.ImageField(default=b'images/None/no-img.jpg', upload_to=b'pic_folder/')),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('agent', models.ForeignKey(blank=True, to='mysite.Agents', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('bedrooms', models.DecimalField(max_digits=4, decimal_places=1)),
                ('heading', models.CharField(max_length=240)),
                ('desc', models.TextField()),
                ('suburb', models.CharField(max_length=200)),
                ('model_pic', models.ImageField(default=b'images/None/no-img.jpg', upload_to=b'pic_folder/')),
                ('featured', models.BooleanField()),
                ('agent', models.ForeignKey(blank=True, to='mysite.Agents', null=True)),
            ],
        ),
    ]
