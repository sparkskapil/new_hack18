# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-31 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0007_auto_20180331_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parameter', models.CharField(max_length=100, null=True)),
                ('Metric', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Image', models.ImageField(blank=True, upload_to='Startup')),
                ('Opportunity', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(max_length=100, null=True)),
                ('Metric', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Metric', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='MarketValidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parameter', models.CharField(max_length=100, null=True)),
                ('Metric', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Problem', models.CharField(max_length=100, null=True)),
                ('ProblemImg', models.ImageField(blank=True, upload_to='Startup')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=100, null=True)),
                ('Sales', models.CharField(max_length=100, null=True)),
                ('Expenses', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Solution', models.CharField(max_length=100, null=True)),
                ('SolutionImg', models.ImageField(blank=True, upload_to='Startup')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='StartupAddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=100, null=True)),
                ('Stage', models.CharField(max_length=100, null=True)),
                ('Logo', models.ImageField(blank=True, upload_to='Startup')),
                ('Website', models.CharField(max_length=100, null=True)),
                ('Tagline', models.CharField(max_length=100, null=True)),
                ('StartupSector', models.CharField(max_length=100, null=True)),
                ('ProductName', models.CharField(max_length=100, null=True)),
                ('ProductImage', models.ImageField(blank=True, upload_to='Startup')),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Designation', models.CharField(max_length=100, null=True)),
                ('Responsiblity', models.CharField(max_length=100, null=True)),
                ('Email', models.CharField(max_length=100, null=True)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Homepage.Startup')),
            ],
        ),
    ]
