# Generated by Django 3.2.5 on 2022-03-24 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('ID', models.UUIDField(default=uuid.UUID('ed50d52e-33ff-4f95-9139-d0c5f9dec7d3'), primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='userImages/')),
                ('name', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('uploadedBy', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='manageImages.picture')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='manageImages.picture')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
