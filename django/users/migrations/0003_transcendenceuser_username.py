# Generated by Django 4.2.7 on 2023-12-03 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_transcendenceuser_creation_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcendenceuser',
            name='username',
            field=models.CharField(default='default', max_length=255, unique=True),
        ),
    ]