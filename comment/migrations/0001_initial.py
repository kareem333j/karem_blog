# Generated by Django 4.1.7 on 2023-02-22 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_admin', models.CharField(default='admin-photo', max_length=30)),
                ('image', models.ImageField(default='photo/5.5.jpg', upload_to='photoss/%y/%m/%d')),
                ('activate', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('comment', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(default='photo/user.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField(max_length=500)),
            ],
        ),
    ]
