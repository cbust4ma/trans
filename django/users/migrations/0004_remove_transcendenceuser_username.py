# Generated by Django 4.2.7 on 2023-12-03 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_transcendenceuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcendenceuser',
            name='username',
        ),
    ]
