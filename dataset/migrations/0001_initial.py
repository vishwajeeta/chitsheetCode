# Generated by Django 4.0 on 2023-08-19 21:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('language', models.CharField(choices=[('solidity', 'solidity')], default='solidity', max_length=50)),
                ('discription', models.TextField()),
                ('information', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
