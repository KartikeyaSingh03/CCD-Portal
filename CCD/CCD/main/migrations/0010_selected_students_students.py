# Generated by Django 2.2.5 on 2020-02-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_userprofile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selected_Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('company', models.CharField(default='', max_length=40)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('Phone_number', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
            ],
        ),
    ]
