# Generated by Django 3.2.9 on 2024-02-22 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatRoom', '0003_rename_room_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='room',
        ),
    ]
