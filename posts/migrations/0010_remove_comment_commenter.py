# Generated by Django 4.0 on 2022-11-23 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_rename_post_comment_commented_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
    ]
