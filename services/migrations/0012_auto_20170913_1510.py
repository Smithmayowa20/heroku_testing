# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-13 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0011_post_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_upload',
            name='post',
        ),
        migrations.RemoveField(
            model_name='image_upload1',
            name='post',
        ),
        migrations.RemoveField(
            model_name='image_upload2',
            name='post',
        ),
        migrations.RemoveField(
            model_name='image_upload3',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='File_upload',
        ),
        migrations.DeleteModel(
            name='Image_upload1',
        ),
        migrations.DeleteModel(
            name='Image_upload2',
        ),
        migrations.DeleteModel(
            name='Image_upload3',
        ),
    ]
