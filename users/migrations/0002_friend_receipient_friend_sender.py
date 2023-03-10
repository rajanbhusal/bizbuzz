# Generated by Django 4.0 on 2022-11-21 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='receipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requestreceipient', to='users.profile'),
        ),
        migrations.AddField(
            model_name='friend',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='requestsender', to='users.profile'),
        ),
    ]
