# Generated by Django 4.0.4 on 2022-05-24 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0006_alter_student_options_rename_gender_student_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('CS', 'CS'), ('DS', 'DS'), ('AI', 'AI'), ('IS', 'IS'), ('IT', 'IT')], default='General', max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.CharField(blank=True, default='0', max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='mail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=8),
        ),
    ]