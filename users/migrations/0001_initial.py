# Generated by Django 4.0 on 2022-11-21 07:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_image', models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('college', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_id', models.CharField(blank=True, max_length=200, null=True)),
                ('twitter_id', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('followers', models.IntegerField(blank=True, default=0, null=True)),
                ('following', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(blank=True, default=0, null=True)),
                ('text_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('receipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends_number', models.IntegerField(blank=True, default=0, null=True)),
                ('friends', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]