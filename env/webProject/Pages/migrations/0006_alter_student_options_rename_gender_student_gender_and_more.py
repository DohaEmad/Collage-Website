# Generated by Django 4.0.4 on 2022-05-24 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0005_user_id_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='GPA',
            new_name='gpa',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='State',
            new_name='state',
        ),
    ]