# Generated by Django 2.2.4 on 2019-12-30 23:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField(blank=True, null=True)),
                ('enrolled_program', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('special_needs', models.BooleanField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('counsellor', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'admission',
            },
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.Admission')),
            ],
            options={
                'db_table': 'fee',
            },
        ),
        migrations.CreateModel(
            name='Slc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insitute_name', models.CharField(max_length=100)),
                ('year_passed', models.DateField(blank=True, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.Admission')),
            ],
            options={
                'db_table': 'slc',
            },
        ),
        migrations.CreateModel(
            name='PlusTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insitute_name', models.CharField(max_length=100)),
                ('year_passed', models.DateField(blank=True, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.Admission')),
            ],
            options={
                'db_table': 'plustwo',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount_paid', models.IntegerField()),
                ('receivedby', models.CharField(max_length=100)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Fee')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insitute_name', models.CharField(max_length=100)),
                ('year_passed', models.DateField(blank=True, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='admission.Admission')),
            ],
            options={
                'db_table': 'master',
            },
        ),
    ]