# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-27 22:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_discussion_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='devis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif', models.IntegerField(null=True)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Client')),
                ('profess', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Prof')),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cont_service', models.CharField(max_length=300)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=8)),
                ('devis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.devis')),
            ],
        ),
    ]
