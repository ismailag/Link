# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-13 14:25
from __future__ import unicode_literals

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
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='a', max_length=30)),
                ('tel', models.IntegerField(blank=True, null=True)),
                ('verification', models.BooleanField(default=False)),
                ('code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Delegation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomd', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gouvernorat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('noms', models.CharField(blank=True, max_length=100)),
                ('fixe', models.IntegerField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('fax', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('verification', models.BooleanField(default=False)),
                ('code', models.IntegerField()),
                ('desc', models.TextField(default='')),
                ('adresse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Delegation')),
            ],
        ),
        migrations.CreateModel(
            name='S_specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_categorie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='s_specialite',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Specialite'),
        ),
        migrations.AddField(
            model_name='prof',
            name='spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.S_specialite'),
        ),
        migrations.AddField(
            model_name='prof',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='delegation',
            name='gouv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Gouvernorat'),
        ),
        migrations.AddField(
            model_name='client',
            name='adresse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Delegation'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
