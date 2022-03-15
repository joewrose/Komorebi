# Generated by Django 3.2.5 on 2022-03-06 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageImages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('vote_type', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='picture',
            name='ID',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(upload_to='userImages/'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
