# Generated by Django 4.0.4 on 2022-05-25 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_password_user_passwordd'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]
