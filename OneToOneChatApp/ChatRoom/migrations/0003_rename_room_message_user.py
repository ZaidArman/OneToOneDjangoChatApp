# Generated by Django 3.2.9 on 2024-02-22 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatRoom', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='user',
        ),
    ]
