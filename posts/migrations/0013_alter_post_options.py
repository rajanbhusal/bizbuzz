# Generated by Django 4.0 on 2022-12-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]